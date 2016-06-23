# -*- coding: utf-8 -*-
import re

from src.tools.calendar import Calendar


class Match(object):
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
        return Match.match_content("\d+", content, "0")

    @staticmethod
    def match_question_id(raw_link):
        u"""
        在链接中匹配question_id，返回文本形式的question_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return Match.match_content("(?<=question/)\d{8}", raw_link)

    @staticmethod
    def match_answer_id(raw_link):
        u"""
        在链接中匹配answer_id，返回文本形式的answer_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return Match.match_content("(?<=answer/)\d{8}", raw_link)

    @staticmethod
    def match_topic_id(raw_link):
        u"""
        在链接中匹配topic_id，返回文本形式的topic_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return Match.match_content("(?<=topic/)\d+", raw_link)

    @staticmethod
    def match_collection_id(raw_link):
        u"""
        在链接中匹配collection_id，返回文本形式的collection_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return Match.match_content("(?<=collection/)\d+", raw_link)

    @staticmethod
    def match_author_id(raw_link):
        u"""
        在链接中匹配author_id，返回文本形式的author_id
        匹配失败返回空字符串
        :type raw_link:str
        :rtype: str
        """
        return Match.match_content("""(?<=people/)[^/'"]+""", raw_link)

    @staticmethod
    def parse_date(date='1357-08-12'):
        u"""
        解析时间,解析失败返回字符串'1357-08-12'
        :type date: str
        :rtype: str
        """
        if u":" in date:
            if u'昨天' in date:
                return Calendar.get_yesterday()
            else:
                return Calendar.get_today()
        if u'今天' in date:
            return Calendar.get_today()
        return Match.match_content(r'\d{4}-\d{2}-\d{2}', date, '1357-08-12')  # 一三五七八十腊，三十一天永不差！
