# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')

# -------------------------------------------------------------------------
# your http://google.com/analytics id
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configure.get('heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

##Clientes##
db.define_table ('clientes',
                 db.Field("id_clientes","id"), 
                 db.Field ('codigo_cliente','integer',label='Código'),
                 db.Field ('nombre','string'),
                 db.Field ('apellido','string'),
                 db.Field ('email','string',label='E-mail'),
                 db.Field ('dni','integer',unique=True,label='D.N.I.'),
                 db.Field ('cuil','string'),
                 db.Field ('genero', label='Género',requires=IS_IN_SET(['Masculino', 'Femenino'])),
                 db.Field ('telefono','integer',label='Teléfono'),
                 db.Field ('direccion','string',label='Dirección'),
                 db.Field ('localidad_cliente','string',label='Localidad'),
                 db.Field ('tipo_categoria', requires=IS_IN_SET(['Resp. Inscr.','Monotributo'])),  
                 db.Field ('provincia','string'),
                 db.Field ('pais','string',label='País'),
                 db.Field ('codigo_postal','integer',label='Código Postal'),
                 db.Field ('estado', requires=IS_IN_SET(['activo','inactivo'])),
                 db.Field ('observaciones','text')
                )

db.clientes.email.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_NOT_IN_DB (db,db.clientes.email)
db.clientes.nombre.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_UPPER(),IS_LENGTH(30)
db.clientes.apellido.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_UPPER(),IS_LENGTH(30)
db.clientes.dni.requires=IS_NOT_IN_DB (db,db.clientes.dni),IS_INT_IN_RANGE(2500000,100000000)
db.clientes.telefono.requires=IS_LENGTH(12, error_message='Solo hasta 12 caracteres')



#db.clientes.localidad_Cliente.requires=IS_IN_DB(db,db.localidad),'%(nombre_localidad)s'
#db.clientes.sexo.requires=IS_IN_SET (['Masculino','Femenino'])

db.define_table ('contacto',
                 db.Field ('nombre','string'),
                 db.Field ('apellido','string'),
                 db.Field ('dni','integer',unique=True,label='D.N.I.'),
                 db.Field ('codigo_postal','integer',label='Código Postal'),
                 db.Field ('email','string',label='E-mail'),
                 db.Field('genero', label='Género',requires=IS_IN_SET(['Masculino', 'Femenino'])),
                 db.Field('telefono','integer',label='Teléfono'),
                 db.Field ('mensaje','text')
                )

db.contacto.email.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_NOT_IN_DB (db,db.contacto.email)
db.contacto.nombre.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_UPPER(),IS_LENGTH(30)
db.contacto.apellido.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_UPPER(),IS_LENGTH(30)
db.contacto.telefono.requires=IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.contacto.dni.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***')

##Vendedor##
db.define_table ('vendedor',
                 db.Field ("id_vendedor","id"), 
                 db.Field ('codigo_vendedor','integer',label='Código'),
                 db.Field ('nombre','string'),
                 db.Field ('apellido','string'),
                 db.Field ('email','string',label='E-mail'),
                 db.Field ('dni','integer',unique=True,label='D.N.I.'),
                 db.Field ('cuil','string'),
                 db.Field ('genero', label='Género',requires=IS_IN_SET(['Masculino', 'Femenino'])),
                 db.Field ('telefono','integer',label='Teléfono'),
                 db.Field ('direccion','string',label='Dirección'),
                 db.Field ('localidad','string'),
                 db.Field ('codigo_postal','integer',label='Código Postal'),
                 db.Field ('observaciones','text')
                )

db.vendedor.nombre.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_UPPER(),IS_LENGTH(30)
db.vendedor.apellido.requires=IS_NOT_EMPTY(error_message='***Campo obligatorio***'),IS_UPPER(),IS_LENGTH(30)
db.vendedor.dni.requires=IS_NOT_IN_DB (db,db.vendedor.dni),IS_INT_IN_RANGE(2500000,100000000)
db.vendedor.telefono.requires=IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
