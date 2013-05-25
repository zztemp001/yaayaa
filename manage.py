#!/usr/bin/env python
#coding=utf-8

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yaayaa.settings")
    curdir = os.path.dirname(__file__)

    # 将通用的模块和开发工具所使用的模块加入到项目路径中
    sys.path.append(os.path.join(curdir, 'yaayaa/packages').replace('\\', '/'))


    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
