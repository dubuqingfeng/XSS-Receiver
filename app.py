#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web
from urls import urls
from setting import settings

__author__ = 'qingfeng'


class RightCateModule(tornado.web.UIModule):
    def render(self, cate_item):
        return self.render_string('modules/right_cate.html', cate_item=cate_item)


if __name__ == "__main__":
    application = tornado.web.Application(
        handlers=urls,
        **settings
    )
    application.listen(8988)
    tornado.ioloop.IOLoop.current().start()