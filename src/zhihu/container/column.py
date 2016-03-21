# -*- coding: utf-8 -*-
from src.zhihu.container.author import Author


class Column(object):
    def __init__(self):
        # 关注数
        self.followers_count = 0

        # 专栏描述
        self.description = u''

        # 专栏个性域名（专栏ID）
        self.slug = u''

        # 专栏名
        self.name = u''

        # 专栏图片地址
        self.avatar_id = u''

        # 已发布文章数
        self.posts_count = 0

        # 创建者
        self.creator = Author()
        return

    def set_followers_count(self, followers_count):
        self.followers_count = followers_count
        return

    def set_description(self, description):
        self.description = description
        return

    def set_slug(self, slug):
        self.slug = slug
        return

    def set_name(self, name):
        self.name = name
        return

    def set_avatar_id(self, avatar_id):
        self.avatar_id = avatar_id
        return
