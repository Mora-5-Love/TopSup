# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/8 20:38
# @desc    : 答题闯关辅助，截屏 ，OCR 识别，百度搜索


from PIL import Image
from common import screenshot, ocr, methods
from threading import Thread
from baiduApiVersion import mjwGetTitleBaiduAndroid
import time

while True:
    # 截图
    start_time = time.clock()
    screenshot.check_screenshot()

    img = Image.open("./screenshot.png")

    # 文字识别
    #  me2_start = time.clock()
    #  me2_end = time.clock()
    #  me2_exit = me2_end - me2_start
    #  print ("me2 time used: \t", me2_exit)
    #  questions, choices = ocr.ocr_img(img)
    question = mjwGetTitleBaiduAndroid.getquestion(img)
    choices = mjwGetTitleBaiduAndroid.getchoices(img)
    # t = time.clock()
    # 用不同方法输出结果，取消某个方法在前面加上#

    # # 打开浏览器方法搜索问题
    # methods.run_algorithm(0, question, choices)
    # # 将问题与选项一起搜索方法，并获取搜索到的结果数目
    # methods.run_algorithm(1, question, choices)
    # # 用选项在问题页面中计数出现词频方法
    # methods.run_algorithm(2, question, choices)

    # 多线程
    m1 = Thread(mjwGetTitleBaiduAndroid.search_from_baidu(question))
    # #  m2 = Thread(methods.run_algorithm(1, question, choices))
    m3 = Thread(methods.run_algorithm(2, question, choices))
    m1.start()
    # #  m2.start()
    m3.start()

    # me2_start = time.clock()
    # #  methods.run_algorithm(2, question, choices)
    # mjwGetTitleBaiduAndroid.search_from_baidu(question)
    # me2_end = time.clock()
    # me2_exit = me2_end - me2_start
    # print ("me2 time used: \t", me2_exit)

    end_time = time.clock()
    exit = end_time - start_time
    print ("time used: \t", exit)

    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    print('------------------------')
