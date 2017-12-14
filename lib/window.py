# -*- coding: utf-8 -*-
import Tkinter
import os
from config import config
import thread
import lxml.html as html
import news
import sys

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root)


@thread.run
def init_window():
    """窗口线程"""
    width = config.get('root', 'width')
    height = config.get('root', 'height')
    origin_x, origin_y = config.get('root', 'x'), config.get('root', 'y')
    root.overrideredirect(True)
    root.attributes('-alpha', config.get('root', 'alpha'))
    root.geometry('%sx%s+%s+%s' % (width, height, origin_x, origin_y))
    canvas.configure(width=width)
    canvas.configure(height=height)
    canvas.configure(bg='black')
    canvas.configure(highlightthickness=0)
    canvas.pack()
    x, y = 0, 0

    def move(event):
        global x, y
        new_x = (event.x-x)+root.winfo_x()
        new_y = (event.y-y)+root.winfo_y()
        root.geometry('%sx%s+%d+%d' % (width, height, new_x, new_y))

    def button_1(event):
        global x, y
        x, y = event.x, event.y
    canvas.bind('<B1-Motion>', move)
    canvas.bind('<Button-1>', button_1)

    button = Tkinter.Button(canvas, text="x", command=close_window, anchor=Tkinter.W)
    button.configure(width=2, activebackground="#000000", background="#000000", fg="white", relief=Tkinter.FLAT)
    button.pack(side=Tkinter.TOP)

    init_news()

    button = Tkinter.Button(canvas, text="……", command=(lambda m=Tkinter.ALL: canvas.delete(m)), anchor=Tkinter.W)
    button.configure(width=4, activebackground="#000000", background="#000000", fg="white", relief=Tkinter.FLAT)
    button.pack(side=Tkinter.BOTTOM)
    news.get_news()
    root.mainloop()


def clear_button():
    canvas.delete(Tkinter.ALL)
    init_news()


def get_news_content():
    print 'test'


def close_window():
    root.quit()
    print '--------退出程序---------'
    sys.exit(0)


def init_news():
    hot_news_list = get_news_list('hot.news')

    for a in hot_news_list:
        button = Tkinter.Button(canvas, text=a.text, command=get_news_content, anchor=Tkinter.W)
        button.configure(width=int(config.get('root', 'width')),  activebackground="#000000", background="#000000",
                         fg="white", relief=Tkinter.FLAT)
        button.pack(side=Tkinter.TOP)
    focus_news_list = get_news_list('focus.news')
    for a in focus_news_list:
        button = Tkinter.Button(canvas, text=a.text, command=get_news_content, anchor=Tkinter.W)
        button.configure(width=int(config.get('root', 'width')),  activebackground="#000000", background="#000000",
                         fg="white", relief=Tkinter.FLAT)
        button.pack(side=Tkinter.TOP)


def get_news_list(news_type):
    news_file_name = os.path.realpath(os.path.dirname('..') + config.get('news', 'output'))
    with open(news_file_name, 'r') as news_file:
        content = news_file.read()
        doc = html.fromstring(content)
        return doc.xpath(config.get('xpath', news_type))


def show_start_msg():
    print '窗口初始化完成！'

