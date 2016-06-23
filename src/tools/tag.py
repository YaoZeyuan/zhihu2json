# -*- coding: utf-8 -*-


class Tag(object):
    """
    工具类,封装基础的Tag方法
    """

    @staticmethod
    def get_content(tag):
        u"""
        提取BeautifulSoup对象中tag.contents的内容
        需要对<br>进行预处理，将<br>换成<br/>,否则会爆栈，
        参考http://palydawn.blog.163.com/blog/static/1829690562012112285248753/
        :type tag: BeautifulSoup
        :rtype: str
        """
        return "".join([unicode(x) for x in tag.contents])

    @staticmethod
    def get_attr(tag, attr, default_value=""):
        u"""
        获取bs中tag.content的指定属性
        若content为空或者没有指定属性则返回默认值
        :type tag: BeautifulSoup
        :type attr: str
        :type default_value: str
        :rtype: str
        """
        if tag is None:
            return default_value
        return tag.get(attr, default_value)
