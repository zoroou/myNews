# -*- coding: utf-8 -*-
import threading


def run(func):
    print '--启动线程: %s--' % func.func_doc
    thread = threading.Thread(target=func)
    thread.start()
    return thread
