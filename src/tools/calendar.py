# -*- coding: utf-8 -*-
import datetime
import time


class Calendar(object):
    u"""
    工具类，提供辅助的日期函数
    """

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
