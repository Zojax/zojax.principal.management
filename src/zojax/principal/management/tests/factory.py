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
from zope import interface, component, schema
from zojax.layoutform import Fields, PageletAddForm
from zojax.controlpanel.interfaces import IPrincipalsManagement
from zojax.principal.management.interfaces import IPrincipalFactory


class IMyPrincipalFactory(IPrincipalFactory):
    pass


class IPrincipal(interface.Interface):

    title = schema.TextLine(
        title = u'Title',
        required = True)


class PrincipalFactory(object):
    interface.implements(IMyPrincipalFactory)
    component.adapts(IPrincipalsManagement, interface.Interface)

    name = __name__ = u'+test.principal'
    title = 'Test Member'
    description = 'Create new test member.'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.__parent__ = context


class AddPrincipalForm(PageletAddForm):

    fields = Fields(IPrincipal)

    label = u'Add new testing principal'
