jquery 使用
***********

技巧
====

``serialize()`` 和 ``serializeArray()``
---------------------------------------

``serialize()`` 方法通过序列化表单值，创建 URL 编码文本字符串。
您可以选择一个或多个表单元素（比如 input 及/或 文本框），或者 form 元素本身。
序列化的值可在生成 AJAX 请求时用于 URL 查询字符串中。 ::

    $("button").click(function(){
        $("div").text($("form").serialize());
    });

返回的字符串类似于： ``a=1&b=2&c=3&d=4&e=5 ``

注释：只会将”成功的控件“序列化为字符串。如果不使用按钮来提交表单，则不对提交按钮的值序列化。
如果要表单元素的值包含到序列字符串中，元素必须使用 name 属性。

``serializeArray()`` 序列化表格元素 (类似 ``serialize()`` 方法) 返回 JSON 数据结构数据。
注意：是 Json 对象，而非 Json 字符串。

一般使用以下函数来讲 ``serializeArray()`` 返回的 Json 对象转换为数组。 ::

    function convertToArray(o) {
        var v = {};
        for (var i in o) {
            if (typeof (v[o[i].name]) == 'undefined') v[o[i].name] = o[i].value;
            else v[o[i].name] += "," + o[i].value;
        }
        return v;
    }

