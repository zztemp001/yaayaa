项目的开发与部署
**************

#. 适用于开发环境和正式运行环境，真正实现无缝结合
#. 使用：django + nginx + gunicorn + fabric + pip + virtualenv

开发环境的差异及解决
=================

#. 开发时使用 ``manage.py runserver`` 运行服务器；部署时使用 ``gunicorn`` 运行服务器， ``IP:PORT`` 都是 **127.0.0.1:8000**
#. 开发时服务器自动 reload，部署时需手动重启 ``gunicorn`` 或使用 ``fabric`` 实现自动重启
#. 在开发机器中设定环境变量 ``developing = True`` ，然后在 ``settings`` 文件中检测此变量，如果检测不到，则意味着是正式运营的机器，
  设置 ``DEBUG = True`` ，同时导入正式运营的 ``settings`` 文件内容。
#. 开发时，修改 ``hosts`` 文件，使 ``www.beetaa.com`` ``static.beetaa.com`` ``media.beetaa.com`` 指向 **127.0.0.1**
  部署时，修改域名记录，使 ``www.beetaa.com`` ``static.beetaa.com`` ``media.beetaa.com`` 指向服务器 IP
#. 开发时，memcached 的 IP 使用 **127.0.0.1**，部署时，使用与开发时同样的设置即可。后期需要扩展的，则在新机器上运行缓存服务


开发环境与部署环境的一致性安排
=========================

#. 项目目录结构保持一致。
#. 通过 ``os.path...`` 来获得项目根目录和设置文件目录
#. 静态文件将归集在 ``yaayaa/public/static`` 目录，设此为 ``settings.STATIC_ROOT`` 的值，``manage.py collectstatic`` 将静态文件拷贝至此
#. 将 ``settings.STATIC_URL`` 设置为 ``/static/`` ，该服务器使用 nginx 运行，并指向以上 ``static`` 目录
#. 网站基本和通用的文件放在 ``yaayaa/static`` 下，下设 ``base`` ``font`` ``icon`` ``site`` ``boot`` 和 ``fav.ico``
#. ``yaayaa/static/boot`` 下设 ``plugins`` ``themes`` 目录
#. 用户上传的文件将存放在 ``yaayaa/public/media`` 目录，设此为 ``settings.MEDIA_ROOT`` 的值，用户上传的文件存放于此
#. 将 ``settings.MEDIA_URL`` 设置为 ``/media/`` ，该服务器使用 nginx 运行，并指向以上 ``static`` 目录
#. 将 nginx 和 fabric 的配置文件放置于项目设置目录下
#. 将网站基础的 ``templates`` ``templatetags`` 放置在项目设置目录下
#. 将数据库文件 ``yaayaa.db`` 放置在项目设置目录下
#. 在开发和部署环境中，都运行 memcached 服务，并在 django 中启动缓存服务
#. 开发和部署时，均启用 logging 模块，日志信息放在设置目录 ``yaayaa/log/yaayaa.log`` 中
#. nginx 日志文件存放在设置目录 ``yaayaa/log/nginx/errors.log`` 中
#. 项目的开发文档统一存放在设置目录 ``yaayaa/docs`` 目录中，其中设 ``notebook`` ``axure`` 目录
#. 系统软件手动进行安装，软件列表清单放在 ``yaayaa/docs/requirements.rst`` 中记录
#. 所有 django app 统一放置在 ``yaayaa/packages`` 目录下，包括开发工具和 **zzpy**
#. 将 pip 的 ``requirements.txt`` 放置在项目设置目录下
#. 将 nginx 的进程号统一存放在 ``yaayaa/nginx.pid`` 下
#.



