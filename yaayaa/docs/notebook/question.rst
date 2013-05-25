问题及思考
**********

开发环境和正式运营环境无缝切换的方案
==============================

#. 使用 ``pip + virtualenv`` 安装 python 依赖库
#. 不能使用 pip 安装的模块放在同一目录下，并将此目录包含至 python 路径
#. 将自己的 ``zzlib`` 库包含至 python 目录下
#. 在开发机器中设定环境变量 ``developing = True`` ，然后在 ``settings`` 文件中
  检测此变量，如果检测不到，则意味着是正式运营的机器，设置 ``DEBUG = True`` ，同时
  导入正式运营的 ``settings`` 文件内容。
#. 用 gunicorn 运行服务器，实现：代码发生变更时，可以自动reload
#. 用 nginx 做反向代理，将 nginx 配置文件放到项目目录下统一管理
#. 在开发机器和运营机器同时安装/启用 memcached，使用本机作为缓存服务器
#. 在开发机器和运营机器上同时启用 logging 记录日志
#. 善用 ``manage.py collectstatics`` 命令，使用 nginx 做静态文件服务器