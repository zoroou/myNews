# -*- coding: utf-8 -*-
import urllib2
import time
from config import config
import thread


@thread.run
def get_news():
    """新闻更新线程"""
    while True:
        result = urllib2.urlopen(config.get('news', 'url')).read()
        html_file = open(config.get('news', 'output'), 'w')
        html_file.write(result)
        html_file.close()
        time.sleep(int(config.get('news', 'update.time')))


def show_start_msg():
    print '新闻更新线程启动完成！'


