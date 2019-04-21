# -*- coding: utf-8 -*-

#
#
# Created by: borlittle 2019/4/21
#
#


import logging
import time

# 创建一个logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
nowTime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
logFile = nowTime + '.log'
fh = logging.FileHandler("logs\\" + logFile)
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
