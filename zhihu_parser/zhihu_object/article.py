# -*- coding: utf-8 -*-
from .author import Author


class Article(object):
    def __init__(self):
        # 发布日期
        self.published_time = u''

        # 作者
        self.author = Author()

        # 所属专栏个性域名
        self.column_slug = u''

        # 所属专栏名
        self.column_name = u''

        # 标题
        self.title = u''

        # 专栏题图
        self.title_image = u''

        # 摘要
        self.summary = u''

        # 内容
        self.content = u''

        # 文章编号
        self.slug = u''

        # 评论数
        self.comments_count = 0

        # 赞同数
        self.likes_count = 0

        return

    def set_published_time(self, published_time):
        self.published_time = published_time
        return

    def set_column_slug(self, column_slug):
        self.column_slug = column_slug
        return

    def set_column_name(self, column_name):
        self.column_name = column_name
        return

    def set_title(self, title):
        self.title = title
        return

    def set_title_image(self, title_image):
        self.title_image = title_image
        return

    def set_summary(self, summary):
        self.summary = summary
        return

    def set_content(self, content):
        self.content = content
        return

    def set_slug(self, slug):
        self.slug = slug
        return

    def set_comments_count(self, comments_count):
        self.comments_count = comments_count
        return

    def set_likes_count(self, likes_count):
        self.likes_count = likes_count
        return
