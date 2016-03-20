# -*- coding: utf-8 -*-
from src.zhihu.container.author import Author


class Answer(object):
    def __init__(self):
        # 答主信息
        self.author = Author()

        # 答案内容(html结构，已经过必要的转换(例如，将<br>替换为<br/>))
        self.content = u''

        # 所属问题id
        self.question_id = 0

        # 答案id
        self.answer_id = 0

        # 答案提交日期
        self.commit_date = u''

        # 答案更新日期
        self.update_date = u''

        # 答案提交日期(精确到秒)
        self.create_time = 1458404150

        # 答案赞同数
        self.votecount = 0

        # 答案评论数
        self.comment_count = 0

        # 标志位

        # 是否已被知乎隐藏
        self.is_hidden = False

        # 是否已被折叠
        self.is_collapsed = False

        # 是否允许转载
        self.is_copyable = True
