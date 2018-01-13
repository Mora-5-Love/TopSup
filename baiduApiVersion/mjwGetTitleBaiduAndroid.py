# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/8 20:38
# @desc    : python 3 , 答题闯关辅助，截屏 ，OCR 识别，百度搜索

import io
import urllib.parse
import webbrowser
import requests
import base64
#  import matplotlib.pyplot as plt
#  import numpy as np
from PIL import Image
import os

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')
def getquestion(img):
    region = img.crop((50, 350, 1000, 600))
    # 百度OCR API  ，在 https://cloud.baidu.com/product/ocr 上注册新建应用即可
    api_key = ''
    api_secret = ''
    # 获取token
    host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+api_key+'&client_secret='+api_secret
    headers = {
        'Content-Type':'application/json;charset=UTF-8'
    }
    res = requests.get(url=host,headers=headers).json()
    token = res['access_token']
    imgByteArr = io.BytesIO()
    region.save(imgByteArr, format='PNG')
    image_data = imgByteArr.getvalue()
    base64_data = base64.b64encode(image_data)
    r = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
                  params={'access_token': token}, data={'image': base64_data})
    # result 即为问题
    result = ''
    for i in r.json()['words_result']:
        result += i['words']
    return result

# searching from baidu
def search_from_baidu(question):
    result = urllib.parse.quote(question)
    webbrowser.open('https://baidu.com/s?wd='+result)

