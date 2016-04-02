# -*- coding: utf-8 -*-
class Question(object):
    def __init__(self):
        # 问题ID
        self.question_id = 0

        # 问题标题
        self.title = u''

        # 问题详情
        self.description = u''

        # 问题相关话题列表
        self.topic_list = []

        # 问题评论数
        self.comments_count = 0

        # 问题关注数
        self.followers_count = 0

        # 问题浏览数
        self.views_count = 0

        # 问题最近活跃日期
        self.active_date = u''

        # 问题答案数
        self.answer_count = 0
        return

    def set_question_id(self, question_id):
        self.question_id = question_id
        return

    def set_title(self, title):
        self.title = title
        return

    def set_description(self, description):
        self.description = description
        return

    def set_topic_list(self, topic_list):
        self.topic_list = topic_list
        return

    def add_topic(self, topic):
        self.topic_list.append(topic)
        return
    
    def set_comments_count(self, comments_count):
        self.comments_count = comments_count
        return

    def set_followers_count(self, followers_count):
        self.followers_count = followers_count
        return

    def set_views_count(self, views_count):
        self.views_count = views_count
        return
