#coding=utf-8

import os
import sys

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = 'http://media.beetaa.com/'
STATIC_URL = 'http://static.beetaa.com/'

ALLOWED_HOSTS = ['.beetaa.com', '127.0.0.1']  # 当 DEBUG=False 时，要设置

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