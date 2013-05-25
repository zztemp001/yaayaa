#coding=utf-8

'''
- 模块： zzpy.system.system
- 描述： 对日常使用的系统工具进行包装，方便使用，包括：
    - 提供后台运行程序的方法

- 作者： 赵伟明 - zztemp001#gmail.com
- 时间： 2013年4月24日 下午 15：26
'''

import subprocess, sys

def run(cmd=''):
    '''
    调用 :py:class:`subprocess.Popen` ，实现程序在后台运行。

    Args:
        cmd (str): 需要运行的 shell 命令
    '''

    if not cmd: return False
    proc = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc

def daemon_in_win32(*args, **kwargs):
    '''让python在windows的隐藏子进程中运行
    also works for Popen.It creates a new *hidden* window, so it will work in frozen apps (.exe).
    '''

    IS_WIN32 = 'win32' in str(sys.platform).lower()

    if IS_WIN32:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        kwargs['startupinfo'] = startupinfo
    retcode = subprocess.call(*args, **kwargs)

    return retcode

if __name__ == "__main__":
    pass
