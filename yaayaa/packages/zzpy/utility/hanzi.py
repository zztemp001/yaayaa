#coding:utf-8

'''
- 模块： zzpy.utility.hanzi
- 描述： 提供操作拼音/汉字的类和函数
    - 取得字符串的拼音
    - 取得字符串各字符拼音的首个字母
    - 取得一个汉字的五笔写法

- 作者： 赵伟明 - zztemp001#gmail.com
- 创建： 2013年4月24日 下午 15：26
'''

import cPickle

class Pinyin():
    def __init__(self):
        f = file('./hanzi.dat') # 将汉字数据库读入文件
        self.dict = cPickle.load(f)
        f.close()

    def pinyin(self, chars=u'', splitter=u'', capital=True):
        '''
        *给出一个字符串，取得该字符串的拼音*

        参数:
            - chars (unicode): 需要转换的中文字符串
            - splitter (unicode): 设置返回的每个字符拼音之间的分隔符，缺省为不分隔
            - capital (Bool): 每个字符的拼音首字母是否大写，缺省为 **True**

        返回:
            - str: 使用分隔符链接起来的拼音字符串，不能转换的汉字将原样返回

        使用方法: ::

            >>> from zzpy.utility.hanzi import Pinyin
            >>> pinyin = Pinyin()
            >>> pinyin.pinyin(u'我是中国人', u' ')
            u'Wo Zhi Zhong Guo Ren'
        '''
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                py = self.dict[key].split("\t")[0].split(" ")[0].strip()[:-1]
                if capital:
                    result.append(py.capitalize())
                else:
                    result.append(py)
            except:
                result.append(char)
        return splitter.join(result)

    def zimu(self, chars=u'', splitter=u'', upper=True):
        '''
        *取得字符串各字符拼音的首个字母*

        参数：
            - chars (unicode): 需要转换的中文字符串
            - splitter (unicode): 字符拼音首位字母之间的分隔符，缺省为不分隔
            - upper (Bool): 字符是否大写，缺省为 **True**

        返回:
            - str: 使用分隔符链接起来的拼音字符串，不能转换的汉字将半角的“?”代替
        '''
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                py = self.dict[key].split("\t")[0].split(" ")[0].strip()[:-1]
                if upper:
                    result.append(py[:1].upper())
                else:
                    result.append(py[:1])
            except:
                result.append(u'?')
        return splitter.join(result)

    def wb(self, char=u'', splitter=u','):
        '''
        *取得一个汉字的五笔写法*

        参数：
            - char (unicode): 需查询的汉字（单字）
            - splitter (unicode): 如果一个汉字有多种五笔方案，则方案之间用此字符分隔

        返回：
            - str: 返回一个字符串，包含一个或多个输入方案，查询不到则返回原字符
        '''
        key = "%X" % ord(char)
        try:
            result = self.dict[key].split("\t")[1].strip()
            result = splitter.join(result.split(" "))
        except:
            result = char
        return result

if __name__ == "__main__":
    p = Pinyin()
    print p.pinyin(u"钓鱼岛是中国的")
    print p.zimu(u'灭了小日本')
    print p.wb(u"国")
