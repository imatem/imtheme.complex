# -*- coding: utf-8 -*-
"""Installer for the imtheme.complex package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='imtheme.complex',
    version='1.0a1',
    description="IM website theme",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Theme",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='python plone theme',
    author='Informática Académica',
    author_email='informatica.academica@matem.unam.mx',
    url='https://github.com/collective/imtheme.complex',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/imtheme.complex',
        'Source': 'https://github.com/collective/imtheme.complex',
        'Tracker': 'https://github.com/collective/imtheme.complex/issues',
        # 'Documentation': 'https://imtheme.complex.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imtheme'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'plone.app.themingplugins',
        # 'collective.themefragments',
        # 'collective.themesitesetup',
        'z3c.jbot',
        # 'plone.api>=1.8.5',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = imtheme.complex.locales.update:update_locale
    """,
)
