gunicorn
********

运行及终止 gunicorn
==================

.. code-block::

    $ gunicorn_django --daemon ./yaayaa/settings_yaayaa.py
    $ killall -9 gunicorn_django

django 设置文件指定时，不能按 ``yaayaa.settings_yaayaa`` 的格式，而是要按设置文件所在路径来。

