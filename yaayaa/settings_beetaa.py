#coding=utf-8

from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# 当 DEBUG=False 时，要设置，内容为系统允许的服务器列表
ALLOWED_HOSTS = ['.beetaa.com', '121.199.35.227', '127.0.0.1']

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


ADMINS = (('admin', 'admin@yaayaa.com'),)

# 配置邮件发送
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'zztemp001'
EMAIL_HOST_PASSWORD = 'z88888888'