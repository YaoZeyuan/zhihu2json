# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def parse(content):
    u"""
    将字符串解析为BeautifulSoup对象,取测试文本中的第一个节点作为Tag进行返回

    :param content: 待解析文本内容
    :type content: unicode
    :rtype: bs4.Tag
    """
    bs = BeautifulSoup(content, u"html.parser")
    dom = bs.select(u"*")[0]
    return dom


def get_content(uri):
    u"""
    获取uri里的文件内容

    :param uri: 文件uri
    :type uri: unicode
    :return: 文件内容
    :rtype:unicode
    """
    content = open(uri, u'r').read()
    return content
