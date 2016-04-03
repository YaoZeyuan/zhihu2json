# -*- coding: utf-8 -*-
from zhihu_parser.content.parse_author import ParseAuthor
from zhihu_parser.tools.parser_tools import ParserTools
from zhihu_parser.tools.debug import Debug
from zhihu_parser.zhihu_object.answer import Answer


class ParseAnswer(ParserTools):
    def __init__(self, dom=None):
        # 初始化基础属性
        self.dom = None
        self.header = None
        self.body = None
        self.footer = None

        self.set_dom(dom)
        self.author_parser = ParseAuthor()
        self.answer = Answer()
        return

    @staticmethod
    def is_hidden(dom):
        # 第二条是为了处理当答案已消失时，知乎仍然将问题显示出来的bug
        return dom.select('div.answer-status') or (not dom.select('textarea.content,div.zm-editable-content'))

    def set_dom(self, dom):
        self.answer = Answer()
        if dom and not ParseAnswer.is_hidden(dom):
            self.dom = dom
            self.header = dom.find('div', class_='zm-item-vote-info')
            self.body = dom.find('div', class_='zm-editable-content')
            self.footer = dom.find('div', class_='zm-meta-panel')
            self.author_parser.set_dom(dom)
        return

    def get(self):
        self.__parse_info()
        author = self.author_parser.get()
        self.answer.set_author(author)
        return self.answer

    def __parse_info(self):
        self.__parse_base_info()
        self.__parse_header_info()
        self.__parse_body_info()
        self.__parse_footer_info()
        return

    def __parse_base_info(self):
        u"""
        解析位于起始div中的信息
        目前有以下三条属性：
        is_collapsed
        is_copyable
        created_time

        :return:
        """
        self.__parse_collapsed_status()
        self.__parse_copyable_status()
        self.__parse_created_time()
        return

    def __parse_collapsed_status(self):
        if not self.has_attr(self.dom, 'data-collapsed'):
            Debug.logger.debug(u'答案折叠状态信息未找到')
        is_collapsed = self.get_attr(self.dom, 'data-collapsed')
        self.answer.set_is_collapsed(is_collapsed)
        return

    def __parse_copyable_status(self):
        if not self.has_attr(self.dom, 'data-copyable'):
            Debug.logger.debug(u'答案转载授权信息未找到')
        is_copyable = self.get_attr(self.dom, 'data-copyable')
        self.answer.set_is_copyable(is_copyable)
        return

    def __parse_created_time(self):
        if self.has_attr(self.dom, 'data-created'):
            Debug.logger.debug(u'答案创建时间戳未找到')
        created_time = self.get_attr(self.dom, 'data-created')
        self.answer.set_created_time(created_time)
        return

    def __parse_header_info(self):
        self.__parse_vote_count()
        return

    def __parse_vote_count(self):
        if not self.header:
            Debug.logger.debug(u'答案赞同数未找到')
        vote_count = self.get_attr(self.header, 'data-votecount')
        self.answer.set_vote_count(vote_count)
        return

    def __parse_body_info(self):
        self.__parse_answer_content()
        return

    def __parse_answer_content(self):
        if not self.body:
            Debug.logger.debug(u'答案内容未找到')
            return
        content = self.get_tag_content(self.body)
        self.answer.set_content(content)
        return

    def __parse_footer_info(self):
        self.__parse_date_info()
        self.__parse_comment_count()
        self.__parse_no_record_flag()
        self.__parse_href_info()
        return

    def __parse_date_info(self):
        u"""
        如果是question类型, 执行这里的, 如果是author类型, 执行simple_answer的
        :return:
        """
        data_block = self.footer.find('a', class_='answer-date-link')
        if not data_block:
            Debug.logger.debug(u'答案更新日期未找到')
            return

        create_date = self.get_attr(data_block, 'data-tip')
        if create_date:
            update_date = data_block.get_text()
            update_date = self.parse_date(update_date)
            create_date = self.parse_date(create_date)
        else:
            create_date = data_block.get_text()
            update_date = create_date = self.parse_date(create_date)
        self.answer.set_create_date(create_date)
        self.answer.set_update_date(update_date)
        return

    def __parse_comment_count(self):
        # BS的属性选择器语法区分“和’！！！
        # 还好知乎所有的属性都是双引号- -
        # 看看人家这软件工程做的！
        # update:看了一下，Tornado强制要求元素属性为双引号。。。汗
        comment = self.footer.select('a[name="addcomment"]')
        if not comment:
            Debug.logger.debug(u'评论数未找到')
            return
        comment_count = self.match_int(comment[0].get_text())
        self.answer.set_comment_count(comment_count)
        return

    def __parse_no_record_flag(self):
        u"""
        之前在dom中已经检测过这个属性，
        现在应该用不到了
        :return:
        """
        copyable_flag = self.footer.find('a', class_='copyright')
        if not copyable_flag:
            Debug.logger.debug(u'禁止转载标志未找到')
            return
        copyable_flag = bool(u'禁止转载' in copyable_flag.get_text())
        self.answer.set_is_copyable(copyable_flag)
        return

    def __parse_href_info(self):
        href_tag = self.footer.find('a', class_='answer-date-link')
        if not href_tag:
            Debug.logger.debug(u'答案href/问题id/答案id未找到')
            return

        raw_href = self.get_attr(href_tag, 'href')
        self.__parse_question_id(raw_href)
        self.__parse_answer_id(raw_href)

        href = "https://www.zhihu.com/question/{0}/answer/{0}".format(self.answer.question_id, self.answer.answer_id)
        self.answer.set_href(href)
        return

    def __parse_question_id(self, href):
        question_id = self.match_question_id(href)
        self.answer.set_question_id(question_id)
        return

    def __parse_answer_id(self, href):
        answer_id = self.match_answer_id(href)
        self.answer.set_answer_id(answer_id)
        return
