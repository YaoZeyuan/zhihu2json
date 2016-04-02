# -*- coding: utf-8 -*-
from .author import Author


class User(Author):
    def __init__(self):
        super(User, self).__init__()

        # 赞同数
        self.votes_count = 0

        # 感谢数
        self.thanks_count = 0

        # 被收藏数
        self.collections_count = 0

        # 被分享数
        self.share_count = 0

        # 提问数
        self.asks_count = 0

        # 回答数
        self.answers_count = 0

        # 专栏文章数
        self.articles_count = 0

        # 公共编辑次数
        self.logs_count = 0

        # 关注的人数
        self.followees_count = 0

        # 粉丝数
        self.followers_count = 0

        # 关注专栏数
        self.column_follows_count = 0

        # 关注话题数
        self.topic_follows_count = 0

        # 被浏览次数
        self.views_count = 0

        # 位置
        self.location = u''

        # 行业
        self.business = u''

        # 性别
        self.gender = u''

        # 公司
        self.employment = u''

        # 职位
        self.position = u''

        # 学校
        self.education = u''

        # 专业
        self.education_extra = u''

        # 微博
        self.weibo = u''
        return

    def set_votes_count(self, votes_count):
        self.votes_count = votes_count
        return

    def set_thanks_count(self, thanks_count):
        self.thanks_count = thanks_count
        return

    def set_collections_count(self, collections_count):
        self.collections_count = collections_count
        return

    def set_share_count(self, share_count):
        self.share_count = share_count
        return

    def set_asks_count(self, asks_count):
        self.asks_count = asks_count
        return

    def set_answers_count(self, answers_count):
        self.answers_count = answers_count
        return

    def set_articles_count(self, articles_count):
        self.articles_count = articles_count
        return

    def set_logs_count(self, logs_count):
        self.logs_count = logs_count
        return

    def set_followees_count(self, followees_count):
        self.followees_count = followees_count
        return

    def set_followers_count(self, followers_count):
        self.followers_count = followers_count
        return

    def set_column_follows_count(self, column_follows_count):
        self.column_follows_count = column_follows_count
        return

    def set_topic_follows_count(self, topic_follows_count):
        self.topic_follows_count = topic_follows_count
        return

    def set_views_count(self, views_count):
        self.views_count = views_count
        return

    def set_location(self, location):
        self.location = location
        return

    def set_business(self, business):
        self.business = business
        return

    def set_gender(self, gender):
        self.gender = gender
        return

    def set_employment(self, employment):
        self.employment = employment
        return

    def set_position(self, position):
        self.position = position
        return

    def set_education(self, education):
        self.education = education
        return

    def set_education_extra(self, education_extra):
        self.education_extra = education_extra
        return

    def set_weibo(self, weibo):
        self.weibo = weibo
        return
