django slugfield
================

作用：是记录的 url 可读性更强，如：可以使用标题作为 url 的一部分。
比如：可以将 ``www.example.com/article/3/`` 这样的url 改为类似于
`` www.example.com/article/America-attack-on-Iraq`` 的方式。

一般的使用方式为 ::

    class Article():
        title = models.CharField(max_length=100)
        content = models.TextField(max_length=1000)
        slug = models.SlugField(max_length=40)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.title) # 保存slug字段，注意不能超过 max_length 的长度
            super(Article, self).save(*args, **kwargs)

        def get_absolute_url(self):
            return reverse('display_article', args=[self.slug])

        # 然后就可以在模板和 view 中使用 {{ object.get_absolute_url }} 得到链接

如果需要将中文转换为拼音，则可以使用 python-slugify https://github.com/un33k/python-slugify ，
或者 uuslug https://github.com/un33k/django-uuslug 。例如 ::

    from uuslug import uuslug as slugify

    s = u'这就是一串中文字，你看得懂吗？'
    print slugify(s)

    >>> zhe-jiu-shi-chuan-zhong-wen-zi-ni-kan-de-dong-ma

