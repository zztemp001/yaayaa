#coding=utf-8

from django.http import HttpResponse

def home(request):
    '''这是一个简单函数

    Args:
        request (Request): django 自带的对象 ::

            0 -- 成功
            1 -- 失败
            2 -- 再试一次

    Returns:
        str 宣染后的页面html

        >>> print get_foobar(10, 20)
        30
        >>> print get_foobar('a', 'b')
        ab

    命令行使用实例 ::

            > mysql --help

    注意：这个view模块 **来源于** :class:`djtest.blog.models.Post` 类

    '''

    return HttpResponse(u'hello, 赵伟明')
