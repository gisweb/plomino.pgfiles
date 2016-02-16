# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plomino.pgfiles.testing import PLOMINO_PGFILES_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that plomino.pgfiles is properly installed."""

    layer = PLOMINO_PGFILES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plomino.pgfiles is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('plomino.pgfiles'))

    def test_browserlayer(self):
        """Test that IPlominoPgfilesLayer is registered."""
        from plomino.pgfiles.interfaces import IPlominoPgfilesLayer
        from plone.browserlayer import utils
        self.assertIn(IPlominoPgfilesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLOMINO_PGFILES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plomino.pgfiles'])

    def test_product_uninstalled(self):
        """Test if plomino.pgfiles is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('plomino.pgfiles'))
