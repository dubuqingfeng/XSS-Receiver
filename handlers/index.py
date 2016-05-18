#!/usr/bin/env python
# coding=utf-8
import tornado

from handlers.base import UserBaseHandler

__author__ = 'qingfeng'


class IndexHandler(UserBaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render('index.html')
