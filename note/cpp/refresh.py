# coding:utf-8


import os
from datetime import datetime


c_basepath = '/mnt/usb16/dev/wyf9/home/note/cpp/'
c_subs = 2

# ----------


def info(log):
    print(f"[Info] [refresh] {datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} " + log)


def run(cmd):
    info(f'Running: echo cd {c_basepath} && {cmd}')
    os.system(f'echo cd {c_basepath} && {cmd}')


def Main():
    for sub in range(1, c_subs + 1):
        run(f'cp _sidebar_sub.md {sub}/_sidebar.md')


if __name__ == '__main__':
    Main()
