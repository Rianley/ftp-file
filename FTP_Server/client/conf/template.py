#!/usr/bin/env python

START_MENU = """
-------------------------------------------
              FTP CLIENT
-------------------------------------------
"""

LOGINED_MENU = """
---------------------------------------------------------------------------------------------
                                    FTP CLIENT

你的名字:{0}         磁盘配额:{1} MB         已经使用:{2} MB
---------------------------------------------------------------------------------------------
Commands:
    put:   put|[文件或文件夹完整路径]      # 上传文件或者文件夹到服务端（请填写完整的路径）
    get:   get|[文件名字]                 # 从服务端下载文件
    show:  show                          # 显示主文件夹下的文件与文件夹
    cd:    cd|[文件夹名字]                # 进入文件夹的下一级目录
    quit:                                # 退出客户端程序
"""
if __name__ =="__main__":
    show_menu = LOGINED_MENU.format('rianley',
                                             str(int(7000000 / 1024 / 1024)),
                                             str(round(70000 / 1024 / 1024,2))),
    print(show_menu)