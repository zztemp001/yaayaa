fabric
******

安装
====

.. code-block::

    $ pip install fabric

范例：获取机器名
==============

#. 在 fabfile.py 中写入以下内容 ::

    from fabric.api import *

    def host_type():
        run('uname -s')

#. 在命令行中运行 ::

    $ fab -H localhost,linuxbox host_type

范例：获取机器名，在 fabfile.py 中指定目标服务器
===========================================

#. 在 fabfile.py 中写入以下内容 ::

    from fabric.api import *

    env.hosts = ['localhost', '22.45.6.23']
    env.user = 'root'

    def host_type():
        run('uname -s')

#. 在命令中运行 ::

    $ fab host_type

范例：更新代码库，重启服务器
========================

#. 在 fabfile_yaayaa.com.py 中写入以下内容 ::

    from fabric.api import *

    env.hosts = ['www.yaayaa.com']
    env.user = 'weiming'

    def update_project():
        # 更新服务器代码并收集静态文件

        with cd('~/sites/yaayaa'):
            run('git pull origin master')
            run('source ~/envs/yaayaa.com/bin/activate')
            run('python manage.py collectstatic --noinput')

    def restart_server():
        # 重启 gunicorn
        run('killall -9 gunicorn_django')
        run('gunicorn_django --daemon ./yaayaa/settings_yaayaa.py')

        # 重启 nginx
        sudo('nginx -s reload')

    def deploy():
        update_project()
        restart_server()



