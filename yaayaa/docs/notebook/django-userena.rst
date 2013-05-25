django-userena
==============

基本信息
--------

    代码仓库：https://github.com/bread-and-pepper/django-userena

依赖
----

    easy_thumbnails：https://github.com/SmileyChris/easy-thumbnails
    django-guardian：https://github.com/lukaszb/django-guardian

设置
----

    #. 将 ``userena``, ``guardian``, ``easy_thumbnails`` 添加到 ``INSTALLED_APPS`` 中
    #. 修改 ``AUTHENTICATION_BACKENDS`` ::

        AUTHENTICATION_BACKENDS = (
            'userena.backends.UserenaAuthenticationBackend',
            'guardian.backends.ObjectPermissionBackend',
            'django.contrib.auth.backends.ModelBackend',
        )

    #. 新建一个用于管理用户的 app，如取名为 ``account`` ::

        >>> manage.py startapp account

    #. 设置电子邮件 - 程序将会发送邮件进行认证。如果是开发时，则忽略此功能 ::

        EMAIL_BANKEND = 'django.core.mail.backends.dummy.EmailBackend'

    #. 如果是生产环境，可以使用 ``SMTP backend`` ::

        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

        EMAIL_USE_TLS = True
        EMAIL_HOST = ‘smtp.gmail.com’
        EMAIL_PORT = 587
        EMAIL_HOST_USER = ‘yourgmailaccount@gmail.com’
        EMAIL_HOST_PASSWORD = ‘yourgmailpassword’

    #. Userena 需要定义一个 profile 类来存放用户的额外信息 ::

        from django.contrib.auth.models import User
        from django.utils.translation import ugettext as _
        from userena.models import UserenaBaseProfile

        class MyProfile(UserenaBaseProfile):
            user = models.OneToOneField(User,
                                        unique=True,
                                        verbose_name=_('user'),
                                        related_name='my_profile')
            favourite_snack = models.CharField(_('favourite snack'),
                                               max_length=5)

        # 如果需要用户可以选择自己的语言，则需要继承 UserenaLanguageBaseProfile 基类
        # 同时在 MIDDLEWARE_CLASSES 中加入 userena.middleware.UserenaLocaleMiddleware

    #. 在项目根目录的 ``urls.py`` 中加入 ::

        (r'^account/', include('userena.urls')),

    #. 在项目 ``settings.py`` 中设置与登录 url 相关的信息 ::

        LOGIN_REDIRECT_URL = '/account/%(username)s/'
        LOGIN_URL = '/account/signin/'
        LOGOUT_URL = '/account/signout/'

    #. 安全设定，在 ``settings.py`` 中 ::

        ANONYMOUS_USER_ID = -1
        AUTH_PROFILE_MODULE = 'accounts.MyProfile'

