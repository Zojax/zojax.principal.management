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
""" zojax.principal.management interfaces

$Id$
"""
from zope import interface
from zope.i18nmessageid import MessageFactory
from zope.viewlet.interfaces import IViewletManager

_ = MessageFactory('zojax.principal.management')


class IPrincipalType(interface.Interface):
    """ principal content type """


class IPrincipalPreferences(interface.Interface):
    """ marker interface for preferences """


class IPrincipalFactory(interface.Interface):
    """ principal factory """

    name = interface.Attribute('Name')

    title = interface.Attribute('Title')

    description = interface.Attribute('Description')

    def __init__(context, request):
        """ adapter factory """


class IPrincipalInformation(IViewletManager):
    """ extra preferences viewlet manager """
