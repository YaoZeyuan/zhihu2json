# -*- coding: utf-8 -*-
import os


class Config(object):
    base_path = os.path.split(os.path.realpath(__file__))[0]
