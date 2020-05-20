.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

======================
imtheme.complex (blue)
======================

Tell me what your product does

Features
--------

- Can be bullet points


Installation
------------

Install imtheme.complex by adding it to your buildout::

    [buildout]

    ...

    eggs =
        imtheme.complex


and then running ``bin/buildout``

Actualización deseada
----------------------

* Desinstalar imtheme.complex
* Configuración del tema: Desactivar Plone Theme: complex
* Desinstalar IM responsivetheme

Actualizacion actual
--------------------

imtheme.complex > blue
matem.congresos > branch themeblue

En ZMI -> portal_setup /Import
* Select Profile imtheme.complex (imblue)
    * imtheme.complex various import handlers Post install import step from imtheme.complex
    * import selected steps
* Configuración del tema: Activar Plone Theme: imblue

* En folder de congresos 2019 seleccionar vista folder_congresos_view
* remplazar vista folder_congresos_view en portal_skins

Contribute
----------

- Issue Tracker: https://github.com/collective/imtheme.complex/issues
- Source Code: https://github.com/collective/imtheme.complex
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
