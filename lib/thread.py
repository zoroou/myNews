# -*- coding: utf-8 -*-
import threading


def run(func):
    print '--启动线程， %s--' % func.func_doc
    threading.Thread(target=func).start()
