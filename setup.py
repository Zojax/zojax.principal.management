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
"""Setup for zojax.principal.management package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='1.2.5dev'


setup(name = 'zojax.principal.management',
      version = version,
      author = 'Nikolay Kim',
      author_email = 'fafhrd91@gmail.com',
      description = "zojax principals management",
      long_description = (
        'Detailed Documentation\n' +
        '======================\n'
        + '\n\n' +
        read('CHANGES.txt')
        ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      url='http://zojax.net/',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax', 'zojax.principal'],
      install_requires = ['setuptools',
                          'zope.component',
                          'zope.interface',
                          'zope.event',
                          'zope.schema',
                          'zope.viewlet',
                          'zope.contentprovider',
                          'zope.i18nmessageid',
                          'zope.app.security',
                          'z3c.traverser',
                          'zojax.layout',
                          'zojax.layoutform',
                          'zojax.controlpanel',
                          'zojax.statusmessage',
                          'zojax.authentication',
                          'zojax.preferences',
                          'zojax.principal.field',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.app.component',
                                  'zope.app.security',
                                  'zope.app.pagetemplate',
                                  'zope.securitypolicy',
                                  'zope.app.security',
                                  'zope.app.zcmlfiles',
                                  'zojax.autoinclude',
                                  'zojax.principal.users',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
