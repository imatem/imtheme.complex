# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from imtheme.complex.testing import IMTHEME_COMPLEX_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that imtheme.complex is properly installed."""

    layer = IMTHEME_COMPLEX_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if imtheme.complex is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'imtheme.complex'))

    def test_browserlayer(self):
        """Test that IImthemeComplexLayer is registered."""
        from imtheme.complex.interfaces import (
            IImthemeComplexLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IImthemeComplexLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IMTHEME_COMPLEX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['imtheme.complex'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if imtheme.complex is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'imtheme.complex'))

    def test_browserlayer_removed(self):
        """Test that IImthemeComplexLayer is removed."""
        from imtheme.complex.interfaces import \
            IImthemeComplexLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IImthemeComplexLayer,
            utils.registered_layers())
