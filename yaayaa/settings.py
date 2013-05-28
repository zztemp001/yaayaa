#coding=utf-8

import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'yaayaa.wsgi.application'
ROOT_URLCONF = 'yaayaa.urls'

SETTINGS_DIR = os.path.dirname(__file__)    # 设置文件所在路径
PROJECT_DIR = os.path.abspath('.')     # 项目根目录所在路径

# 将通用的模块和开发工具所使用的模块加入到项目路径中
sys.path.append(os.path.join(SETTINGS_DIR, 'packages').replace('\\', '/'))

# 设置用户上传内容的目录和 url
MEDIA_ROOT = os.path.join(SETTINGS_DIR, 'public/media/').replace('\\', '/')
MEDIA_URL = '/media/'

# 设置网站静态内容的目录和 url
STATIC_ROOT = os.path.join(SETTINGS_DIR, 'public/static/').replace('\\', '/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(SETTINGS_DIR, 'static/').replace('\\', '/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# 设置模板文件的目录和加载器所在路径
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_DIR, 'templates/').replace('\\', '/'),
    os.path.join(PROJECT_DIR, 'account/templates/').replace('\\', '/'),
)

# 模板上下文预处理
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

# 设置中间件列表和加载顺序
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)

# 配置使用/停用的 app 列表
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 启用后台管理
    'django.contrib.admin',
    'django.contrib.admindocs',
    # 开发工具
    'debug_toolbar',
    'south',
    'autofixture',
    # 底层功能
    'ajax',
    'crispy_forms',
    'mptt',
    # 通用功能
    #'guardian',
    'taggit',
    'userena',
    'userena.contrib.umessages',
    'categories',
    # 对外实现模块
    'account',
    'blog',
)

# 配置 django-userena
LOGIN_REDIRECT_URL = '/account/%(username)s/'
USERENA_SIGNIN_REDIRECT_URL = LOGIN_REDIRECT_URL
LOGIN_URL = '/account/signin/'
LOGOUT_URL = '/account/signout/'
AUTH_PROFILE_MODULE = 'account.Profile'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140
ANONYMOUS_USER_ID = -1

# 配置用户认证的 backend
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# 配置 debug_toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# 配置 logging 功能，详细参考：http://docs.djangoproject.com/en/dev/topics/logging
# 此处配置：当 DEBUG=False 时，如遇 500 错误，则将 logging 信息发送至 admin
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SETTINGS_DIR, 'yaayaa.db').replace('\\', '/'),
        }
}

# 语言/时区设置
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'utf-8'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 其他设置
ADMINS = (('admin', 'admin@yaayaa.com'),)
MANAGERS = ADMINS
SITE_ID = 1
SECRET_KEY = 'g@$6#q-w@jc-skrf2%=g-g85$b+3yy6z-7f27b-8wh@#bvwvkd'

# 配置邮件发送
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 如非开发机器，则引入正式设置覆盖当前开发设置
#if not os.environ.get("DEVELOPING"):
#    from deploy_settings import *