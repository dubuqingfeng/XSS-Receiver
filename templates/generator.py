# coding=utf-8
import codecs
import json

import sys
from imp import reload

reload(sys)
sys.setdefaultencoding("utf-8")

list_test = ['xss', 12]
dict_test = {
    "name": "xss",
    "slug": "xss",
    "desc": "xss test",
    "parameter": "test",
    "configuration parameters": list_test,
}
f = codecs.open("xss.desc", "w", encoding="utf-8")
f.write(json.dumps(dict_test, ensure_ascii=False).encode('utf8'))
f.close()
