#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib


def translate(q):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=huacicha&\
key=199079426&type=data&doctype=json&version=1.1&q=' + q
    data = json.loads(urllib.urlopen(url).read())
    code = data['errorCode']
    if 20 == code:
        print '遇到错误：要翻译的文本过长!'
    elif 30 == code:
        print '遇到错误：无法进行有效的翻译!'
    elif 40 == code:
        print '遇到错误：不支持的语言类型!'
    elif 50 == code:
        print '遇到错误：无效的KEY!'
    else:
        print '#' * 58
        print u'查询：%s' % data['query']
        print u'翻译：%s' % data['translation'][0]
        try:
            print u'发音：/%s/' % data['basic']['phonetic']
        except Exception:
            pass
        try:
            explains = data['basic']['explains']
            print '-' * 25 + u'基本释义' + '-' * 25
            for i in explains:
                print u'%s' % i
        except Exception:
            pass
        try:
            web = data['web']
            print '-' * 25 + u'网络释义' + '-' * 25
            for i in web:
                print '%s: %s' % (i['key'], ','.join(i['value']))
        except Exception:
            pass
        print '#' * 58

if __name__ == '__main__':
    s = sys.argv[1]
    translate(s)
