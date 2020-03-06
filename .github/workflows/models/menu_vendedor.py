# -*- coding: utf-8 -*-

# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('For sale'), XML('&trade;&nbsp;'), # LOGO SDP
                  _class="navbar-brand", _href="index",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

if auth.has_membership(group_id='vendedor'):
    response.menu = [
        (T('Inicio'), False, URL('default', 'index'), [])
    ]


    response.menu += [
                (T('Agregar'), False, '#',[
                    (T('Vendedor'), False, URL('agregar', 'agregar_vendedor'),[]),
                    (T('Medicamento'), False, URL('agregar', 'agregar_productos'),[]),
                    (T('Cliente'), False, URL('agregar', 'agregar_cliente'),[])
                                        ])]
    
    
    
    response.menu += [
                (T('Lista'), False, '#',[
                    (T('Vendedores'), False, URL('consultas', 'reportes_vendedor'),[]),
                    (T('Clientes'), False, URL('consultas', 'reportes_clientes'),[]),
                    (T('Medicamentos'), False, URL('consultas', 'reportes_productos'),[]),
                    ])]
    
    response.menu += [
                (T('Mensajes'), False, '#',[
                    (T('Contactos'), False, URL('consultas', 'reportes_contacto'),[]),
     ])]
                 
DEVELOPMENT_MENU = True

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------

if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
