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
        :param tag: 待提取对象
        :type tag: bs4.Tag
        :return:
        :rtype: unicode
        """
        return u"".join([unicode(x) for x in tag.contents])

    @staticmethod
    def get_attr(tag, attr, default_value=u""):
        u"""
        获取bs中tag.content的指定属性
        若content为空或者没有指定属性则返回默认值

        :param tag: 待提取对象
        :type tag: bs4.Tag
        :param attr: 待获取属性
        :type attr: unicode
        :param default_value: 当属性不存在时返回的默认值
        :type default_value: unicode
        :return: tag中的指定属性，不存在返回默认值
        :rtype: str
        """
        if tag is None:
            return default_value
        return tag.get(attr, default_value)
