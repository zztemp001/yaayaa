#coding=utf-8

from fabric.api import *

env.hosts = ['www.yaayaa.com']
env.user = 'weiming'

def update_project():
    # 更新服务器代码并收集静态文件
    with cd('~/sites/yaayaa'):
        run('git pull origin master')
        with prefix('source ~/envs/yaayaa.com/bin/activate'):
            run('python manage.py collectstatic --noinput')

def restart_server():
    # 重启 gunicorn
    try:
        run('killall -9 gunicorn_django')
    except:
        pass

    run('gunicorn_django -D ./yaayaa/settings_yaayaa.py')

    # 重启 nginx
    sudo('nginx -s reload')

def deploy():
    run('uname -s')
    update_project()
    restart_server()