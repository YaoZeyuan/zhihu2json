# -*- coding: utf-8 -*-
class Topic(object):
    def __init__(self):
        # 话题ID
        self.id = u''

        # 话题名
        self.title = u''

        # 话题描述
        self.description = u''

        # 话题关注数
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

    def set_followers_count(self, followers_count):
        self.followers_count = followers_count
        return
