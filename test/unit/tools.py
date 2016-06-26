# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def parse(content, selector, index=0):
    u"""
    将字符串解析为BeautifulSoup对象

    :param content: 待解析文本内容
    :type content: str
    :param selector: css选择器
    :type selector: str
    :param index: 目标元素为第几个元素
    :type index: int
    :rtype: BeautifulSoup
    """
    bs = BeautifulSoup(content, "html.parser")
    dom = bs.select(selector)[index]
    return dom


def get_content(uri):
    u"""
    获取uri里的文件内容

    :param uri: 文件uri
    :type uri: str
    :return: 文件内容
    :rtype:str
    """
    content = open(uri, 'r').read()
    return content
