# -*- coding: utf-8 -*-
import re

import time

import datetime

from bs4 import BeautifulSoup


class ParseTools(object):
    """
    工具类
    """

    @staticmethod
    def match_content(patten, content, default=""):
        u"""
        在给定的文本中匹配第一个符合正则参数的部分，未匹配到则返回default值
        :type patten: str
        :type content: str
        :type default: str
        :rtype: str
        """
        result = re.search(patten, str(content))
        if result is None:
            return default
        return result.group(0)

    @staticmethod
    def match_int(content):
        u"""
        返回文字中最长的数字串(文本形式)，若没有则返回文本'0'
        :type content:str
        :rtype: str
        """
        return ParseTools.match_content("\d+", content, "0")

    @staticmethod
    def match_question_id(raw_link):
        u"""
        在链接中匹配question_id，返回文本形式的question_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return ParseTools.match_content("(?<=question/)\d{8}", raw_link)

    @staticmethod
    def match_answer_id(raw_link):
        u"""
        在链接中匹配answer_id，返回文本形式的answer_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return ParseTools.match_content("(?<=answer/)\d{8}", raw_link)

    @staticmethod
    def match_topic_id(raw_link):
        u"""
        在链接中匹配topic_id，返回文本形式的topic_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return ParseTools.match_content("(?<=topic/)\d+", raw_link)

    @staticmethod
    def match_collection_id(raw_link):
        u"""
        在链接中匹配collection_id，返回文本形式的collection_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return ParseTools.match_content("(?<=collection/)\d+", raw_link)

    @staticmethod
    def match_author_id(raw_link):
        u"""
        在链接中匹配author_id，返回文本形式的author_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return ParseTools.match_content("""(?<=people/)[^/'"]+""", raw_link)

    @staticmethod
    def get_tag_content(tag):
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

    @staticmethod
    def parse_date(date='1357-08-12'):
        u"""
        解析时间,解析失败返回字符串'1357-08-12'
        :type date: str
        :rtype: str
        """
        if u":" in date:
            if u'昨天' in date:
                return ParseTools.get_yesterday()
            else:
                return ParseTools.get_today()
        if u'今天' in date:
            return ParseTools.get_today()
        return ParseTools.match_content(r'\d{4}-\d{2}-\d{2}', date, '1357-08-12')  # 一三五七八十腊，三十一天永不差！

    @staticmethod
    def get_timestamp():
        u"""
        获取当前时间戳
        :rtype:str
        """
        return str(time.time()).split('.')[0]

    @staticmethod
    def get_today():
        u"""
        获取形如2016-06-23的当前日期
        :rtype:str
        """
        return datetime.date.today().isoformat()

    @staticmethod
    def get_yesterday():
        u"""
        获取形如2016-06-23的昨天的文本字符串
        :rtype:str
        """
        today = datetime.date.today()
        one = datetime.timedelta(days=1)
        yesterday = today - one
        return yesterday.isoformat()
