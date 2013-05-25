URL 分发
========

Django 通过 ``urls.py`` 模块进行 url 映射。
因为是纯 python 代码，所以可以动态对这一模块进行修改。
即，可以动态生成 **url pattern** 到函数的映射。

Django 处理请求的流程
--------------------

#. 首先，Django 会决定最上一级的 url 配置。正常情况下，Django 会使用 ``settings.py`` 中的
  ``ROOT_URLCONF`` 设置。但如果在请求的 ``HttpRequest`` 对象中设置了 ``urlconf``，该值将
  覆盖 ``ROOT_URLCONF``。

#. Django 加载该 url 设置模块，并从中查找变量 ``urlpatterns`` ，该变量应该是由
  ``django.conf.urls.patterns()`` 函数生成的一个 *list* 。

#. Django 按配置文件的顺序查找与请求 url 相一致的 **url pattern** 。一旦找到匹配的，Django
  将调用相应的 ``view`` 函数，并将一个 ``HttpRequest`` 对象作为其第一个参数传递过去。 请求中如
  果包含有其他参数的，将随之一并传递过去（在 ``HttpRequest`` 之后）。

#. 如果没有任何匹配项，或在此过程中有任何其他错误，Django 将会调用相应的错误处理 ``view`` 进行处理。

范例
----

以下是一个简单的 ``URLconf`` 例子 ::

    from django.conf.urls import patterns, url

    urlpatterns = patterns('',
        url(r'^articles/2003/$', 'news.views.special_case_2003'),
        url(r'^articles/(\d{4})/$', 'news.views.year_archive'),
        url(r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),
        url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),
    )

以上例子使用前缀（patterns 函数的第一个参数）可以写成 ::

    urlpatterns = patterns('news.views',
        url(r'^articles/2003/$', 'special_case_2003'),
        url(r'^articles/(\d{4})/$', 'year_archive'),
        url(r'^articles/(\d{4})/(\d{2})/$', 'month_archive'),
        url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'article_detail'),
    )

#. 要捕抓 url 中的值，只需要在需要捕抓的地方加上小括号。

#. 不要在前面使用 ``/`` ，如：使用 ``^articles/`` ，而不是 ``/articles/`` 。

#. 在每一个正则表达式字符串前加上一个 ``r`` ，可以保证字符串不会被提前转义处理。

通过命名组来传递命名参数
---------------------

以上的例子通过按位置的先后来传递参数。如果需要传递命名参数，则可以使用正则表达式的命名组功能。
使用方法是通过在匹配模式前加上 ``?P<name>`` ，如 ::

    urlpatterns = patterns('',
        url(r'^articles/2003/$', 'news.views.special_case_2003'),
        url(r'^articles/(?P<year>\d{4})/$', 'news.views.year_archive'),
        url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'news.views.month_archive'),
        url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'news.views.article_detail'),
    )

以上 **url pattern** 将匹配以下 **view** ::

    news.views.year_archive(request, year='2003')
    news.views.month_archive(request, year='2005', month='03')
    news.views.article_detail(request, year='2003', month='03', day='03')


URLconf 查找的对象说明
---------------------

URLconf 查找请求的 url，但不包含域名、GET/POST/HEAD 等数据。
例如，对于 ``http://www.example.com/myapp/`` ，将会查找其中的 ``myapp/`` 。
对于 ``http://www.example.com/myapp/?page=3`` ，查找的内容同样也是 ``myapp/`` 。

不管在匹配模式中使用何种类型来匹配，捕抓到的参数都将作为 **纯字符串** 传递给 view 。
如对于：``url(r'^articles/(?P<year>\d{4})/$', 'news.views.year_archive'),`` ，
虽然 ``\d{4}`` 只匹配到数字样式的字符串，但传递给 view 时，一样是 **纯字符串** 。
因此，要 **记住在 view 中先将传递过来的字符串转换为需要使用的类型。**

错误处理
--------

如果 Django 找不到相应的匹配模式，或者发生错误，则会调用相应的 view 来进行反馈、处理。
用户可以自定义错误处理的 view ，包括 ``handler404`` ``handler500`` ``handler403`` 。
这几个变量要在最上一级的 ``urls.py`` 中设定，否则无效。缺省情况下，其值为 ::

    handler404 = 'django.views.defaults.page_not_found'
    handler500 = 'django.views.defaults.server_error'
    hanlder403 = django.views.defaults.permission_denied

URLconf 可以从包含它的父级 URLconf 中获取捕获的参数信息
---------------------------------------------------

例如 ::

    # In settings/urls/main.py
    urlpatterns = patterns('',
        url(r'^(?P<username>\w+)/blog/', include('foo.urls.blog')),
    )

    # In foo/urls/blog.py
    urlpatterns = patterns('foo.views',
        url(r'^$', 'blog.index'),
        url(r'^archive/$', 'blog.archive'),
    )

父级中捕获的 ``username`` 变量将如期被传递至 ``foo.views.blog.archive`` 中。

