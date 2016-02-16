# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plomino.pgfiles


class PlominoPgfilesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plomino.pgfiles)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plomino.pgfiles:default')


PLOMINO_PGFILES_FIXTURE = PlominoPgfilesLayer()


PLOMINO_PGFILES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLOMINO_PGFILES_FIXTURE,),
    name='PlominoPgfilesLayer:IntegrationTesting'
)


PLOMINO_PGFILES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLOMINO_PGFILES_FIXTURE,),
    name='PlominoPgfilesLayer:FunctionalTesting'
)


PLOMINO_PGFILES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLOMINO_PGFILES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlominoPgfilesLayer:AcceptanceTesting'
)
