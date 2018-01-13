
# 答题辅助(mjw-dev)
## 使用步骤 (百度 OCR)

请移步详细帮助，[链接](/baiduApiVersion)

#### 1. 安装 ADB

下载地址：https://adb.clockworkmod.com/
安装完后插入安卓设备且安卓已打开 USB 调试模式，终端输入 `adb devices` ，显示设备号则表示成功。我手上的机子是坚果 pro1，第一次不成功,查看设备管理器有叹号，使用 [handshaker](https://www.smartisan.com/apps/handshaker) 加载驱动后成功，也可以使用豌豆荚之类的试试。
#### 2. 安装 python 3
#### 3. 安装所需 python 包

命令行：
```
pip install pytesseract
pip install pillow  
pip install requests

```
#### 4. 在 `GetTitleBaiduAndroid.py` 中加入相应 key

```
百度OCR API
api_key = ''
api_secret = ''
```

#### 5. 运行脚本
`python mjwGetQuestionTessAndroid.py`
会自动识别文字并打开浏览器
