# -*- coding: utf-8 -*-

#
#
# Created by: borlittle 2019/4/21
#
#


import logging
import time
import sys

# create a logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# create a  handler, write into file
nowTime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
logFile = nowTime + '.log'
fh = logging.FileHandler("logs\\" + logFile)
fh.setLevel(logging.DEBUG)

# create a  handler, output to the console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# give the format of handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add handler to logger
logger.addHandler(fh)
logger.addHandler(ch)
