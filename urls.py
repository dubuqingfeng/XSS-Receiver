#!/usr/bin/env python
# coding=utf-8
from handlers import login, index

__author__ = 'qingfeng'

urls = [
    (r"/admin", index.IndexHandler),
    (r"/admin/login", login.LoginHandler),
    (r"/admin/myjs", index.MyJSHandler),
    (r"/admin/templates", index.TemplateHandler),
    (r"/admin/receiver", index.ReceiverHandler),
    (r"/admin/configs", index.ConfigsHandler),
    (r"/admin/addproject", index.AddProjectHandler),
    (r"/admin/project", index.ProjectHandler),
    (r"/project/%s", index.MyJSHandler),
]
