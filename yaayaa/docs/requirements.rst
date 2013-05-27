开发及部署环境
************

系统级别软件安装
==============

.. code-block:: shell

    # 安装编译环境
    $ sudo apt-get install build-essential
    $ sudo apt-get install python-dev

    # 安装 git
    $ sudo apt-get install git

    # 安装 nginx + memcached + pylibmc
    $ sudo apt-get install nginx
    $ sudo apt-get install memcached
    $ sudo apt-get install python-pylibmc

    # 安装 pillow 包所依赖的库文件
    $ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev

    # 安装并启用 virtualenv + pip
    $ sudo apt-get install python-setuptools
    $ sudo easy_install virtualenv
    $ virtualenv ~/env/yaayaa
    $ source ~/env/yaayaa/bin/activate

virtualenv 基本模块安装
======================

.. code-block:: shell

    # 安装 django 1.5.1
    $ pip install django=1.5.1

    # 安装 gunicorn
    $ pip install gunicorn

    # 安装 fabric （需要 build-essential + python_dev）
    $ pip install fabric

    # 安装 PIL/pillow
    $ pip install pillow

virtualenv 依赖模块安装
=====================

.. code-block:: shell

    # 安装 easy_thumbnails (django-userena)
    $ pip install easy_thumbnails

    # 安装 decorator (django-ajax)
    $ pip install decorator

django 应用功能模块安装
=====================

.. code-block:: shell

    # 安装 django-guardian (django-userena，权限管理）
    $ pip install django-guardian



