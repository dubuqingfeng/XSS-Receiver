#!/usr/bin/env python
# coding=utf-8
import hashlib
import os

from handlers.base import BaseHandler

__author__ = 'qingfeng'


def encrypt(password):
    salt = "d811630c4e62c6ef90d1bfe540212aaf"
    return get_md5(get_md5(get_md5(salt, password), password), password)


def get_md5(salt, password):
    string = '%s%s%s' % (salt, password, salt)
    return hashlib.new("md5", string.encode('utf-8')).hexdigest()


class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print(encrypt('admin'))
        if self.get_current_user():
            self.redirect(self.get_argument('next', '/admin'))
        else:
            self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if (username == os.getenv('USERNAME', 'admin')) and (encrypt(password) == os.getenv('PASSWORD', 'c33ba20b52f8aa5a8699deee49b54218')):
            self.set_secure_cookie("user", username)
            self.redirect(self.get_argument('next', '/admin'))
        else:
            self.write("<script>alert('Access Denied')</script>")
            self.render('login.html')


class LogoutHandler(BaseHandler):
    def get(self):
        if self.get_argument("logout", None):
            self.clear_all_cookies()
            self.redirect("/")
        self.redirect("/")
