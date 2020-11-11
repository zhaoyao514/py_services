# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 4:28 下午
# @Author  : ZYAO
# @File    : rename_files.py
# @Software: PyCharm
# @Description : 重命名文件夹下所有文件

import os
path = '../天气预报表情包/30度以上'
files = os.listdir(path)
for i, file in enumerate(files):
    NewFileName = os.path.join(path, str(i)+'.jpg')
    OldFileName = os.path.join(path, file)
    os.rename(OldFileName, NewFileName)