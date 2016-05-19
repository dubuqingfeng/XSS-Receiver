import os

from pymongo import MongoClient

__author__ = 'qingfeng'

THEME = 'default/'
client = MongoClient('mongodb://%s:%s@%s:%s/' % (
    os.getenv('MONGODB_USER', 'admin'), os.getenv('MONGODB_PASS', 'mypass'),
    os.getenv('MONGODB_PORT_27017_TCP_ADDR', '192.168.99.100'), os.getenv('MONGODB_PORT_27017_TCP_PORT', '27017')))
