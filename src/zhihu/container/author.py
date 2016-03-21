# -*- coding: utf-8 -*-
class Author(object):
    def __init__(self):
        # 用户名
        self.name = u''

        # 头像
        self.logo = u''

        # 签名
        self.bio = u''

        # 用户id/md5值（可用于唯一确定用户身份）
        self.id = u''

        # 用户个性域名（可以被用户自由修改）
        self.slug = u''
        return

    def set_name(self, name):
        self.name = name
        return

    def set_logo(self, logo):
        self.logo = logo
        return

    def set_bio(self, bio):
        self.bio = bio
        return

    def set_id(self, id):
        self.id = id
        return

    def set_slug(self, slug):
        self.slug = slug
        return
