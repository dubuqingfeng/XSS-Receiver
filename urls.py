#!/usr/bin/env python
# coding=utf-8
from handlers import login, index

__author__ = 'qingfeng'


urls = [
    (r"/admin/login", login.LoginHandler),
    (r"/admin", index.IndexHandler)
]