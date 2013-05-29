#coding=utf-8

from fabric.api import *

env.hosts = ['www.beetaa.com']
env.user = 'root'

def update_project():
    # 更新服务器代码并收集静态文件
    with cd('/root/prj/yaayaa'):
        run('git pull origin master')
        with prefix('source /root/env/mytest/bin/activate'):
            run('python manage.py collectstatic --noinput')

def restart_server():
    # 重启 gunicorn
    try:
        run('killall -9 gunicorn_django')
    except:
        pass

    with cd('/root/prj/yaayaa'):
        with prefix('source /root/env/mytest/bin/activate'):
            run('gunicorn_django -D ./yaayaa/settings_beetaa.py')

    # 重启 nginx
    with cd('/root/prj/yaayaa'):
        sudo('cp ./yaayaa/nginx_beetaa.conf /etc/nginx/nginx.conf')
    sudo('nginx -s reload')

def deploy():
    run('uname -s')
    update_project()
    restart_server()