#coding=utf-8

'''
- 模块： zzpy.system.logger
- 描述： 对 python 自带的 :py:class:`logging.Logger` 进行包装，方便使用
- 作者： 赵伟明 - zztemp001#gmail.com
- 时间： 2013年4月24日 下午 15：26
'''

import logging, time

class Logger():
    '''
    对python自带的logging进行包装。使用方法 ::

    >>> from zzpy.system.logger import Logger
    >>> logger = Logger('mylog.log')
    >>> logger.p_log(u'尝试写入日志信息')

    日志文件将按如下格式记录内容 ::

    [2012-11-14 12:12:33,390]  尝试写入日志信息
    '''

    log_file = 'log.txt'    # 缺省的日记文件
    log_level = logging.DEBUG   # 设置记录级别为 DEBUG
    logger = logging.getLogger()    # 初始化 logger，用于实际操作日志

    def __init__(self, log_file=None):
        '''
        初始化 logger 类

        Args:
            log_file: 记录 log 信息的文件名，缺省为同目录下的 ``log.txt``
        '''

        if type(log_file) is str: self.log_file = log_file

        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter("[%(asctime)s]  %(message)s")

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(self.log_level)

    def p_log(self, msg=u''):
        '''
        向日志文件写入 log 信息

        Args:
            msg: 写入的信息内容，缺省为空字符串。应使用 **unicode**
        '''
        print '[ %s ]  %s' % (str(time.asctime()), msg)
        self.logger.log(self.log_level, msg=msg)

if __name__ == "__main__":
    logger = Logger()
    logger.p_log('程序行ioooo')