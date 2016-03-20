# -*- coding: utf-8 -*-
class Author(object):
    def __init__(self):
        # 用户名
        self.name = u''

        # 头像
        self.logo = u''

        # 签名
        self.sign = u''

        # 用户md5值（可用于唯一确定用户身份）
        self.md5 = u''

        # 用户个性域名（可以被用户自由修改）
        self.id = u''
        return
