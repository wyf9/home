#coding:utf-8
import os

def go(dir, name, start, end):
    dir=str(dir)
    name=str(name)
    for i in range(start, end+1):
        os.system(f"cd {dir} && mv {name}-{i}.md {i}.md")


go('/mnt/usb16/dev/wyf9/home/note/cpp/1', 1, 1, 37)
go('/mnt/usb16/dev/wyf9/home/note/cpp/2', 2, 1, 8)
