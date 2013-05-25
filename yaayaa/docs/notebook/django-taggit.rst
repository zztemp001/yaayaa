django-taggit
=============

基本信息
--------

    代码仓库：https://github.com/alex/django-taggit



依赖
----

    无

安装
----

    #. 将 ``taggit`` 目录放置在 ``Python Path`` 下
    #. 将 ``"taggit"`` 添加至 ``INSTALLED_APPS``
    #. 使用 ``south`` 生成/跟踪数据表 ::

        >>>manage.py migrate taggit

使用
----

    #. 在任何需要使用 ``taggit`` 的 **model** 中加入 ::

        from django.db import models

        from taggit.managers import TaggableManager

        class Food(models.Model):
            # 字段定义

            tags = TaggableManager()  # tags 将作为表单的字段

    #. 使用 ``ModelForm`` 或 ``Form`` 生成表单

taggit 使用空格/半角逗号/半角双引号作为分隔标志
------------------------------------------

例如：

====================== ================================= ================================================
Tag input string       Resulting tags                    Notes
====================== ================================= ================================================
apple ball cat         ``["apple", "ball", "cat"]``      No commas, so space delimited
apple, ball cat        ``["apple", "ball cat"]``         Comma present, so comma delimited
"apple, ball" cat dog  ``["apple, ball", "cat", "dog"]`` All commas are quoted, so space delimited
"apple, ball", cat dog ``["apple, ball", "cat dog"]``    Contains an unquoted comma, so comma delimited
apple "ball cat" dog   ``["apple", "ball cat", "dog"]``  No commas, so space delimited
"apple" "ball dog      ``["apple", "ball", "dog"]``      Unclosed double quote is ignored
====================== ================================= ================================================

``commit = False``
------------------

当在保存记录时使用了 ``commit = False`` 时，需要另行加入 ``save_m2m()`` ,否则 tag 信息将不会保存 ::

    if request.method == "POST":
        form = MyFormClass(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # 如果没有以下这一句，tag 信息将不会被保存
            form.save_m2m()

过滤
----

使用标准的 **Django ORM API** 来筛选 ``tag`` 。
如：有一个 ``Food`` 的 model，一个应用了 ``TaggableManager`` 的 ``tags`` 字段。
要找出所有 **delicious** 的字段 ::

    >>> Food.objects.filter(tags__name__in=["delicious"])
    [<Food: apple>, <Food: pear>, <Food: plum>]

对于多重筛选来说，通常会产生重复的结果，这就要使用 ``distinct()`` ::

    >>> Food.objects.filter(tags__name__in=["delicious", "red"])
    [<Food: apple>, <Food: apple>]
    >>> Food.objects.filter(tags__name__in=["delicious", "red"]).distinct()
    [<Food: apple>]
