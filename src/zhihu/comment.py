# -*- coding: utf-8 -*-
from src.zhihu.author import Author


class Comment(object):
    def __init__(self):
        self.href = u''
        self.id = 0
        self.author = Author()
        self.content = u''
        self.created_time = u''
        self.likes_count = 0
        self.is_reply_to = False
        self.reply_to_user = Author()
        return

    def set_href(self, href):
        self.href = href
        return

    def set_id(self, id):
        self.id = id
        return

    def set_content(self, content):
        self.content = content
        return

    def set_created_time(self, created_time):
        self.created_time = created_time
        return

    def set_likes_count(self, likes_count):
        self.likes_count = likes_count
        return

    def set_is_reply_to(self, is_reply_to):
        self.is_reply_to = is_reply_to
        return
