# -*- coding: utf-8 -*-
class Author(object):
    def __init__(self):
        # 用户名
        self.name = u''

        # 头像图片id
        self.avatar_id = u''

        # 签名
        self.bio = u''

        # 用户hash值（可用于唯一确定用户身份）
        self.hash = u''

        # 用户个性域名（可以被用户自由修改）
        self.slug = u''

        # 用户描述
        self.description = u''
        return

    def set_name(self, name):
        self.name = name
        return

    def set_avatar_id(self, avatar_id):
        self.avatar_id = avatar_id
        return

    def set_bio(self, bio):
        self.bio = bio
        return

    def set_hash(self, hash):
        self.hash = hash
        return

    def set_slug(self, slug):
        self.slug = slug
        return

    def set_description(self, description):
        self.description = description
        return
