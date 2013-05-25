django-ajax
===========

基本信息
--------

    代码仓库：https://github.com/joestump/django-ajax

依赖
----

    decorator：https://pypi.python.org/pypi/decorator ::

        pip install decorator

初始化
------

    #. 将 ``ajax`` 目录添加至 **Python Path** 中
    #. 将 ``"ajax"`` 添加至 ``INSTALLED_APPS``
    #. 在 ``urls.py`` 中添加 ``(r'^ajax/', include('ajax.urls'))``
    #. 在需要使用 ``ajax`` 的 *app* 目录下添加文件 ``endpoints.py`` 用于统一书写 *endpoint* 代码

使用
----

    #. **Ad-hoc Endpoint** 模式。

    对于 ``/ajax/{some_app_name}/{some_endpoint}.json`` 这样的调用形式，
    将被视为一种 *ad-hot endpoint* 调用。以上调用将被映射至 ``some_app_name.endpoints.some_endpoint`` 。
    函数 ``some_app_name`` 需要返回一个 ``dict`` 或 ``HttpResponse`` 。系统将自动转换为 ``json`` 格式。

    #. **Model Endpoint 新增** 模式。

    对于 ``/ajax/{some_app_name}/{model}.json`` 这样的调用形式，
    将被视为一种 *ModelEndpoint* 调用。以上调用将 **直接** 对 ``model`` 进行一个 **新增记录** 操作。

    #. **Model Enpoint 记录操作** 模式。

    对于 ``/ajax/{some_app_name}/{model}/{pk}/(update|delete|get).json`` 这样的调用形式。
    将被视为对某一特定 **pk** 的记录进行 ``update`` ``delete`` ``get`` 操作。

Ad-hoc Endpoint
---------------

    #. ad-hoc endpoints 的书写与一般的 django views 无异
    #. 所有正常的 *view decorators* 都可以使用，比如 ``@login_required`` 等
    #. 传递的参数只能是一个 ``request`` ，不能有其他参数
    #. 必须返回一个 **dict** 或者 **HttpResponse**
    #. 请使用 ``ajax.exceptions.AJAXError`` 返回错误信息

    **以下例子简单的返回用户提交的 POST 数据：**

    #. 在文件 ``endpoints.py`` 中 ::

        from ajax.exceptions import AJAXError

        def right_back_at_you(request):
            if len(request.POST):
                return request.POST
            else:
                raise AJAXError(500, 'Nothing to echo back.')

    #. 在客户端的 ``js`` 文件中 ::

        $.post('/ajax/my_app/right_back_at_you.json', {
            name: "Joe Stump",
            age: 31},
            function(data) {
                alert(data);
            });

使用 ``ajax.encoders.encoder`` 将 django 的 record/queryset 转换为 json
---------------------------------------------------------------------

    比如 ::

        from ajax.encoders import encoder
        encoder.encode(record)

