#!/usr/bin/env python
# coding=utf-8
import codecs
import datetime
import json
import os

from handlers.base import UserBaseHandler

__author__ = 'qingfeng'


class IndexHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


def get_templates(file_dir):
    default_directory = os.path.join(os.path.dirname(__file__), file_dir)
    templates = []
    try:
        for f in os.listdir(default_directory):
            if f.endswith(".desc"):
                desc_file = codecs.open(default_directory + "/" + f, 'r', encoding="utf-8")
                jsonobj = json.load(desc_file)
                templates.append(jsonobj)
    except OSError:
        print("Failed to access: %s" % dir)
    return templates


class MyJSHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        templates = get_templates('../myjs')
        self.render('myjs.html', templates=templates)


class TemplateHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        templates = get_templates('../templates')
        self.render('templates.html', templates=templates)


class ReceiverHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        contents = self.db.content.find()
        content_items = []
        for content in contents:
            content_items.append(content)
        self.render('receiver.html', contents=content_items)


class ConfigsHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        projects = self.db.project.find()
        project_items = []
        ##查看js
        for project in projects:
            project['count'] = self.db.content.find().count()
            print(project)
            project_items.append(project)
        self.render('configs.html', projects=project_items)


class AddProjectHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        myjs = get_templates('../myjs')
        public = get_templates('../templates')
        self.render('addproject.html', myjs=myjs, public=public)

    def post(self, *args, **kwargs):
        project_name = self.get_argument("project_name")
        project_desc = self.get_argument("project_desc")
        project_public = self.get_arguments("public")
        project_myjs = self.get_arguments("myjs")
        project_custom = self.get_argument("project_custom")

        project_db = self.db.project
        project = project_db.find_one({"project_name": project_name})
        if not project:
            project_item = {
                "project_name": project_name,
                "project_desc": project_desc,
                "project_add_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "project_public": project_public,
                "project_myjs": project_myjs,
                "project_custom": project_custom
            }
            project_id = project_db.insert_one(project_item)
            js_file_content = ''
            # 生成js
            for public in project_public:
                js_file_content += get_js("../templates/", public)
            for myjs in project_myjs:
                js_file_content += get_js("../myjs/", myjs)
            js_file_content += project_custom

            project_directory = os.path.join(os.path.dirname(__file__), "../static/project/")
            js_file = codecs.open(project_directory + project_name + ".js", 'w', encoding="utf-8")
            js_file.write(js_file_content)
            js_file.close()
            if project_id:
                self.redirect(self.get_argument('next', '/admin/configs'))
        else:
            self.redirect(self.get_argument('next', '/admin/addproject'))


def get_js(file_dir, file_name):
    default_directory = os.path.join(os.path.dirname(__file__), file_dir)
    js_file = codecs.open(default_directory + file_name + ".js", 'r', encoding="utf-8")
    return js_file.read()


class ProjectHandler(UserBaseHandler):
    def get(self, *args, **kwargs):
        global js_file
        project_name = self.get_argument("name")
        project_directory = os.path.join(os.path.dirname(__file__), "../static/project/")
        project = {
            "project_name": project_name
        }
        try:
            js_file = codecs.open(project_directory + project_name + ".js", 'r', encoding="utf-8")
        except FileNotFoundError:
            print("FileNotFoundError")
            project['js_file'] = 'File Not Found.'
        else:
            project['js_file'] = js_file.read()
        self.render('project_desc.html', project=project)
