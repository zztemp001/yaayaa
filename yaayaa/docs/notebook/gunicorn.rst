gunicorn
********

运行 gunicorn
=============

.. code-block::

    $ gunicorn --bind 127.0.0.1:8000 --daemon --settings yaayaa.settings_yaayaa yaayaa.wsgi:applicatoin

