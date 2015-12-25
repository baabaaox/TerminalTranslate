#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A bash translate tool for ubuntu
'''

import json
import urllib
import argparse


def translate(q):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=huacicha&\
key=199079426&type=data&doctype=json&version=1.1&q=' + q
    try:
        data = json.loads(urllib.urlopen(url).read())
    except Exception:
        print '网络故障'
        return False
    code = data['errorCode']
    if 20 == code:
        print '遇到错误：要翻译的文本过长!'
    elif 30 == code:
        print '遇到错误：无法进行有效的翻译!'
    elif 40 == code:
        print '遇到错误：不支持的语言类型!'
    elif 50 == code:
        print '遇到错误：无效的KEY!'
    elif 60 == code:
        print '无词典结果，仅在获取词典结果生效!'
    else:
        print '#' * 58
        print u'查询：%s' % data['query']
        print u'翻译：%s' % data['translation'][0]
        try:
            print u'美式发音：/%s/' % data['basic']['us-phonetic']
        except Exception:
            pass
        try:
            print u'英式发音：/%s/' % data['basic']['uk-phonetic']
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

    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument(
        '-w',
        '--word',
        type=str,
        default='translate',
        help='the word need translate'
    )
    args = parser.parse_args()
    translate(args.word)
