#!/usr/bin/env python
# coding=utf-8

import os
import configs
__author__ = 'qingfeng'

_basedir = os.path.abspath(os.path.dirname(__file__))

settings = {
    "template_path": os.path.join(_basedir, 'themes/', configs.THEME, 'templates'),
    "static_path": os.path.join(_basedir, 'static'),
    "debug": True,
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/admin/login",
}