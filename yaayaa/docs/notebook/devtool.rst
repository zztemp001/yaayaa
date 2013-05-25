项目配置
========

django-debug-toolbar
--------------------

#. 将 ``debug_toolbar`` 目录拷贝至 Python 可以找到的路径下
#. 将以下内容添加至 ``settings.py`` 的 ``MIDDLEWARE_CLASSES`` 中的 **最后一行** ::

  'debug_toolbar.middleware.DebugToolbarMiddleware',

#. 在 ``settings.py`` 设置以下变量 ::

  INTERNAL_IPS = ('127.0.0.1',)

#. 将 ``debug_toolbar`` 包添加至 ``settings.py`` 中的 ``INSTALLED_APPS``
#. 在 ``settings.py`` 中设置 ``DEBUG_TOOLBAR_PANELS`` 变量，可配置显示的面板 ::

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

south
-----

#. 将 ``south`` 添加至 ``INSTALLED_APPS`` 中
#. 运行 ``manage.py syncdb`` 将 south 数据表添加中数据库
#. 将其他 app 添加至 ``INSTALLED_APPS`` 中
#. 对每个 app 分别运行 ``manage.py schemamigration app_name --initial``，它将在每个 app 的目录下创建 ``migration`` 目录和相应的文件
#. 对于刚刚创建的项目（未 syncdb 过的），使用命令 ``manage.py migrate app_name``
#. 对于之前已经 syncdb 过的 app，使用命令 ``manage.py migrate app_name 0001 --fake``