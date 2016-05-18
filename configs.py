import os

from pymongo import MongoClient

__author__ = 'qingfeng'

THEME = 'default/'
client = MongoClient('mongodb://admin:mypass@192.168.99.100:27017/')