# -*- coding: utf-8 -*-
from src.zhihu.container.author import Author


class Comment(object):
    def __init__(self):
        # 评论id
        self.id = 0

        # 评论内容
        self.content = u''

        # 评论作者
        self.author = Author()

        # 回复给
        self.reply_to = Author()

        # 赞同数
        self.votecount = 0

        return
