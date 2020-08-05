#!/usr/bin/env python
"""
客户端配置文件
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 服务端地址
FTP_SERVER_IP = "127.0.0.1"
FTP_SERVER_PORT = 9999
# 文件下载保存路径
DOWNLOAD_FILE_PATH = os.path.join(BASE_DIR, "download")
# 日志文件存放路径
LOGS = os.path.join(BASE_DIR, "logs/ftpclient.log")
