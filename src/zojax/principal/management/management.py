##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import schema, interface, component
from zope.component import getAdapters, getUtility, queryMultiAdapter

from zope.publisher.interfaces import NotFound
from zope.app.security.vocabulary import PrincipalSource
from zope.app.security.interfaces import IAuthentication, PrincipalLookupError

from zojax.principal.field import PrincipalField
from zojax.layoutform import button, Fields, PageletForm
from zojax.preferences.interfaces import IPreferenceGroup
from zojax.statusmessage.interfaces import IStatusMessage
from zojax.controlpanel.interfaces import IPrincipalsManagement

from interfaces import _
from interfaces import IPrincipalFactory
from interfaces import IPrincipalPreferences


class IManagementView(interface.Interface):

    principal = PrincipalField(
        title = _('Principal'),
        description = _(u"Select principal to view/edit."),
        required =  True)


class ManagementView(PageletForm):
    interface.implements(IPrincipalsManagement)

    label = _('Select principal')
    fields = Fields(IManagementView)
    ignoreContext = True

    def factories(self):
        factories = []
        for name, factory in getAdapters(
            (self.context, self.request), IPrincipalFactory):
            factories.append((factory.title, name, factory))

        factories.sort()
        return [factory for t,n,factory in factories]

    @button.buttonAndHandler(_(u'View principal'))
    def handleView(self, action):
        data, errors = self.extractData()

        if errors or not data['principal']:
            IStatusMessage(self.request).add(
                _(u'Please select principal.'), 'warning')
        else:
            self.redirect('%s/@@index.html'%data['principal'])


class TraverserPlugin(object):
    component.adapts(IPrincipalsManagement, interface.Interface)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def publishTraverse(self, request, name):
        context = self.context

        view = queryMultiAdapter((context, request), name=name)
        if view is not None:
            return view

        try:
            principal = getUtility(IAuthentication).getPrincipal(name)
        except PrincipalLookupError:
            raise NotFound(context, name, request)

        root = getUtility(IPreferenceGroup)
        root = root.__bind__(principal, context)
        root.__name__ = name

        interface.alsoProvides(root, IPrincipalPreferences)
        return root
