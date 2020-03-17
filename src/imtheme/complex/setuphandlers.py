# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'imtheme.complex:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    avisos = api.content.get('/inicio/1/2/copy_of_avisos/')
    avisos.setTitle('AVISOS')
    avisos = api.content.get('/inicio/1/2/copy_of_movimiento-academico')
    avisos.setTitle('INTERCAMBIO ACADÉMICO')
    # menu
    act = api.content.get('/actividades')
    act.setTitle('Actividades académicas')
    act.reindexObject(idxs=['Title'])
    act = api.content.get('/servicios')
    act.setTitle('Servicios internos')
    act.reindexObject(idxs=['Title'])
    for name in ['/docencia', '/divulgacion', '/vinculacion', '/unidad']:
        act = api.content.get(name)
        act.setExcludeFromNav(True)
        act.reindexObject()
    portal = api.portal.get()
    portal.moveObject('servicios', 18)
    biblio = api.content.create(type='Folder', title='Bibliotecas', container=portal)
    api.content.transition(obj=biblio, transition='publish_internally')
    api.content.transition(obj=biblio, transition='publish_externally')
    portal.moveObject('bibliotecas', 18)

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
