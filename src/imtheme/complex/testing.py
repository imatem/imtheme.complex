# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import imtheme.complex


class ImthemeComplexLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=imtheme.complex)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'imtheme.complex:default')


IMTHEME_COMPLEX_FIXTURE = ImthemeComplexLayer()


IMTHEME_COMPLEX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMTHEME_COMPLEX_FIXTURE,),
    name='ImthemeComplexLayer:IntegrationTesting',
)


IMTHEME_COMPLEX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMTHEME_COMPLEX_FIXTURE,),
    name='ImthemeComplexLayer:FunctionalTesting',
)


IMTHEME_COMPLEX_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IMTHEME_COMPLEX_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ImthemeComplexLayer:AcceptanceTesting',
)
