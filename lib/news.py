# -*- coding: utf-8 -*-
import urllib2
import time
import sys
from config import config

stop = False


def get_news():
    """新闻更新"""
    result = urllib2.urlopen(config.get('news', 'url')).read()
    html_file = open(config.get('news', 'output'), 'w')
    html_file.write(result)
    html_file.close()


def show_start_msg():
    print '新闻更新线程启动完成！'

