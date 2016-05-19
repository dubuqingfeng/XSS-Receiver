#!/usr/bin/env python
# coding=utf-8
import datetime

from handlers.base import UserBaseHandler

__author__ = 'qingfeng'


class IndexHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class MyJSHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        self.render('myjs.html')


class TemplateHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        self.render('templates.html')


class ReceiverHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        receiver = self.db.receiver.find()
        self.render('receiver.html')


class ConfigsHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        projects = self.db.project.find()
        project_items = []
        ##查看js
        for project in projects:
            project_items.append(project)
        self.render('configs.html', projects=project_items)


class AddProjectHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        self.render('addproject.html')

    def post(self, *args, **kwargs):
        project_name = self.get_argument("project_name")
        project_desc = self.get_argument("project_desc")
        project_public = self.get_arguments("public")
        project_myjs = self.get_arguments("myjs")

        project_db = self.db.project
        project = project_db.find_one({"project_name": project_name})
        if not project:
            project_item = {
                "project_name": project_name,
                "project_desc": project_desc,
                "project_add_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "project_public": project_public,
                "project_myjs": project_myjs
            }
            project_id = project_db.insert_one(project_item)
            #生成js
            if project_id:
                self.redirect(self.get_argument('next', '/admin/configs'))
        else:
            self.render('addproject.html')


class ProjectHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        project_name = self.get_argument("name")
        pass
