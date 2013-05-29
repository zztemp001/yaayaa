nginx
*****

media/static 目录的正确配置
=========================

.. code-block::

    server {
        listen 80;

        location /media/ {
            root /root/prj/yaayaa/yaayaa/public;    #此处的路径设根路径，须在该目录下新建 media 目录
        }

        location /static/ {
            root /root/prj/yaayaa/yaayaa/public;    #此处的路径设根路径，须在该目录下新建 static 目录
        }
    }

目录权限的解决
============

解决办法：http://stackoverflow.com/questions/6795350/nginx-403-forbidden-for-all-files

.. code-block:: shell

    # 查看是否有权限
    $ namei -ox /root

    # 如果没有，则需要添加
    $ chmod o+x /root

启动、停止、重启 nginx 进程
========================

.. code-block:: shell

    # 使用缺省配置文件启动
    prompt> nginx

    # 使用指定配置文件启动
    prompt> nginx -c 配置文件路径

    # 修改配置后平滑重启
    prompt> nginx -s reload
    # 或者使用
    prompt> nginx -HUP 主进程号/进程号文件路径（.pid）

    # 查找 nginx 主进程号
    prompt> ps -ef | grep nginx

    # 使用主进程号停止 nginx
    prompt> kill -QUIT/-TERM 主进程号/进程号文件路径（.pid）

    # 强制停止 nginx
    prompt> pkill -9 nginx

测试配置文件是否正确
=================

.. code-block:: shell

    # 测试缺省配置文件
    prompt> nginx -t

    # 测试指定配置文件
    prompt> nginx -t -c 配置文件路径

nginx 可用变量列表
=================

.. code-block::

    $args #这个变量等于请求行中的参数。
    $content_length #请求头中的Content-length字段。
    $content_type #请求头中的Content-Type字段。
    $document_root #当前请求在root指令中指定的值。
    $host #请求主机头字段，否则为服务器名称。
    $http_user_agent #客户端agent信息
    $http_cookie #客户端cookie信息
    $limit_rate #这个变量可以限制连接速率。
    $request_body_file #客户端请求主体信息的临时文件名。
    $request_method #客户端请求的动作，通常为GET或POST。
    $remote_addr #客户端的IP地址。
    $remote_port #客户端的端口。
    $remote_user #已经经过Auth Basic Module验证的用户名。
    $request_filename #当前请求的文件路径，由root或alias指令与URI请求生成。
    $query_string #与$args相同。
    $scheme #HTTP方法（如http，https）。
    $server_protocol #请求使用的协议，通常是HTTP/1.0或HTTP/1.1。
    $server_addr #服务器地址，在完成一次系统调用后可以确定这个值。
    $server_name #服务器名称。
    $server_port #请求到达服务器的端口号。
    $request_uri #包含请求参数的原始URI，不包含主机名，如：”/foo/bar.php?arg=baz”。
    $uri #不带请求参数的当前URI，$uri不包含主机名，如”/foo/bar.html”。
    $document_uri #与$uri相同。

