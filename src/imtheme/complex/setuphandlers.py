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
    avisos.reindexObject(idxs=['Title'])
    intercambio = api.content.get('/inicio/1/2/copy_of_movimiento-academico')
    intercambio.setTitle('INTERCAMBIO ACADÉMICO')
    intercambio.reindexObject(idxs=['Title'])

    # Rename menu items
    act = api.content.get('/actividades')
    act.setTitle('Actividades académicas')
    act.reindexObject(idxs=['Title'])
    servicios = api.content.get('/servicios')
    servicios.setTitle('Servicios internos')
    servicios.reindexObject(idxs=['Title'])

    # hide items
    for name in ['/docencia', '/vinculacion', '/unidad']:
        item = api.content.get(name)
        item.setExcludeFromNav(True)
        item.reindexObject()

    # new content
    portal = api.portal.get()
    biblio = api.content.create(type='Folder', title='Bibliotecas', container=portal)
    api.content.transition(obj=biblio, transition='publish_internally')
    api.content.transition(obj=biblio, transition='publish_externally')

    # sort
    portal.moveObject('fsd', 2)
    portal.moveObject('divulgacion', 4)
    portal.moveObject('actividades', 5)
    portal.moveObject('seminarios', 6)
    portal.moveObject('bibliotecas', 7)
    portal.moveObject('servicios', 8)
    putils = api.portal.get_tool(name='plone_utils')
    putils.reindexOnReorder(portal)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
