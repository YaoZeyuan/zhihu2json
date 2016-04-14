# -*- coding: utf-8 -*-
from zhihu_parser.tools.parser_tools import ParserTools
from zhihu_parser.tools.debug import Debug

from zhihu_parser.zhihu_object.author import Author


class ParseAuthor(ParserTools):
    """
    实践一把《代码整洁之道》的做法，以后函数尽量控制在5行之内
    """

    def __init__(self, dom=None):
        # 初始化基础属性
        self.dom = None
        self.author = Author()

        self.set_dom(dom)
        return

    def set_dom(self, dom):
        self.author = Author()
        if dom:
            self.dom = dom.find('div', class_='zm-item-answer-author-info')
        return

    def get(self):
        self.__parse()
        return self.author

    def __parse(self):
        if (not self.dom.find('img')) and (not self.dom.find('a', class_='author-link')):
            self.__create_anonymous_author()
        else:
            self.__parse_author_info()
        return

    def __parse_author_info(self):
        self.__parse_author_slug()
        self.__parse_author_bio()
        self.__parse_author_logo()
        self.__parse_author_name()
        return

    def __create_anonymous_author(self):
        self.author.set_slug(u'zhihuAPI')
        self.author.set_hash(u'NiMingYongHu')
        # 匿名用户专用头像
        self.author.set_avatar_id(u'da8e974dc')
        self.author.set_name(u'匿名用户')
        return

    def __parse_author_slug(self):
        author = self.dom.find('a', class_='zm-item-link-avatar')
        if not author:
            author = self.dom.find('a', class_='author-link')  # for collection
        if not author:
            Debug.logger.debug(u'用户ID未找到')
            return
        link = self.get_attr(author, 'href')
        author_slug = self.match_author_slug(link)
        self.author.set_slug(author_slug)
        return

    def __parse_author_bio(self):
        u"""
        解析用户签名
        :return:
        """
        bio = self.dom.find('strong', class_='zu-question-my-bio')
        if not bio:
            bio = self.dom.find('span', class_='bio')
        if not bio:
            Debug.logger.debug(u'用户签名未找到')
            return
        author_bio = self.get_attr(bio, 'title')
        self.author.set_bio(author_bio)
        return

    def __parse_author_logo(self):
        u"""
        解析用户logo
        :return:
        """
        author_logo = self.get_attr(self.dom.find('img'), 'src')
        avatar_id = self.match_author_avatar_id(author_logo)
        self.author.set_avatar_id(avatar_id)
        return

    def __parse_author_name(self):
        name = self.dom.find('a', class_='author-link')
        if not name:
            Debug.logger.debug(u'用户名未找到')
            return
        author_name = name.text
        self.author.set_name(author_name)
        return
