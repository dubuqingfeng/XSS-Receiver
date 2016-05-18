#!/usr/bin/env python
# coding=utf-8
import os

from handlers.base import BaseHandler

__author__ = 'qingfeng'


def encrypt(password):
    return password


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        if self.get_current_user():
            self.redirect(self.get_argument('next', '/'))
        else:
            self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if (username == os.getenv('USERNAME', 'admin')) and (encrypt(password) == os.getenv('PASSWORD', 'admin')):
            self.set_secure_cookie("user", username)
            self.redirect(self.get_argument('next', '/'))
        else:
            self.write("<script>alert('Access Denied')</script>")
            self.render('login.html')


class LogoutHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        if self.get_argument("logout", None):
            self.clear_all_cookies()
            self.redirect("/")
        self.redirect("/")
