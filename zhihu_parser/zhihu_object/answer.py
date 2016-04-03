# -*- coding: utf-8 -*-
from .author import Author


class Answer(object):
    def __init__(self):
        # json数据
        self.json_dict = {}

        # 答主信息
        self.author = Author()

        # 答案内容(html结构，已经过必要的转换(例如，将<br>替换为<br/>))
        self.content = u''

        # 所属问题id
        self.question_id = 0

        # 答案id
        self.answer_id = 0

        # 答案提交日期
        self.create_date = u''

        # 答案更新日期
        self.update_date = u''

        # 答案提交日期(精确到秒)
        self.create_time = 1458404150

        # 答案赞同数
        self.vote_count = 0

        # 答案评论数
        self.comment_count = 0

        # 标志位

        # 是否已被知乎隐藏
        self.is_hidden = False

        # 是否已被折叠
        self.is_collapsed = False

        # 是否允许转载
        self.is_copyable = True

        return

    def set_question_id(self, question_id):
        self.question_id = question_id
        self.json_dict['question_id'] = question_id
        return

    def set_answer_id(self, answer_id):
        self.answer_id = answer_id
        self.json_dict['answer_id'] = answer_id
        return

    def set_content(self, content):
        self.content = content
        self.json_dict['content'] = content
        return

    def set_create_date(self, create_date):
        self.create_date = create_date
        self.json_dict['create_date'] = create_date
        return

    def set_update_date(self, update_date):
        self.update_date = update_date
        self.json_dict['update_date'] = update_date
        return

    def set_create_time(self, create_time):
        self.create_time = create_time
        self.json_dict['create_date'] = create_time
        return

    def set_vote_count(self, vote_count):
        self.vote_count = vote_count
        self.json_dict['vote_count'] = vote_count
        return

    def set_comment_count(self, comment_count):
        self.comment_count = comment_count
        self.json_dict['comment_count'] = comment_count
        return

    def set_is_hidden(self, is_hidden):
        is_hidden = bool(is_hidden)
        self.is_hidden = is_hidden
        self.json_dict['is_hidden'] = is_hidden
        return

    def set_is_collapsed(self, is_collapsed):
        is_collapsed = bool(is_collapsed)
        self.is_collapsed = is_collapsed
        self.json_dict['is_collapsed'] = is_collapsed
        return

    def set_is_copyable(self, is_copyable):
        is_copyable = bool(is_copyable)
        self.is_copyable = is_copyable
        self.json_dict['is_copyable'] = is_copyable
        return