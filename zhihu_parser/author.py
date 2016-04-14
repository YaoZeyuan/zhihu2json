# -*- coding: utf-8 -*-
from zhihu_parser.base import BaseParser
from zhihu_parser.info.author import AuthorInfo


class AuthorParser(BaseParser):
    def get_extra_info(self):
        author = AuthorInfo(self.dom)
        return author.get_info()
