# -*- coding: utf-8 -*-
from src.zhihu.author import Author


class Collection(object):
    def __init__(self):
        # 收藏夹ID
        self.id = u''

        # 收藏夹名
        self.title = u''

        # 收藏夹描述
        self.description = u''

        # 收藏夹评论数
        self.comments_count = 0

        # 收藏夹创建者
        self.creator = Author()

        # 最近活跃日期
        self.active_date = u''

        # 关注数
        self.followers_count = 0
        return

    def set_id(self, id):
        self.id = id
        return

    def set_title(self, title):
        self.title = title
        return

    def set_description(self, description):
        self.description = description
        return

    def set_comments_count(self, comments_count):
        self.comments_count = comments_count
        return

    def set_active_date(self, active_date):
        self.active_date = active_date
        return

    def set_followers_count(self, followers_count):
        self.followers_count = followers_count
        return
