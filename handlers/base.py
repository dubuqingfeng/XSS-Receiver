#!/usr/bin/env python
# coding=utf-8

import tornado.web
import configs

__author__ = 'qingfeng'


class BaseHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.db = configs.client.xssreceiver

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return self.get_secure_cookie("user")


class UserBaseHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        print('test')

    @tornado.web.authenticated
    def prepare(self):
        pass
