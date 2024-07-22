#!/bin/python3
# coding: utf-8

import os
import sys
devdir = '/mnt/usb16/dev/'

if not len(sys.argv) < 2:
    un = sys.argv[1]
    a = sys.argv[2]
    n1 = os.path.join(devdir, f'.wyf9/cpp/study/{un}/{a}.cpp')
    n1d = os.path.join(devdir, f'.wyf9/cpp/study/{un}/')
    n2 = os.path.join(devdir, f'wyf9/home/note/cpp/{un}/{a}.md')
    n2d = os.path.join(devdir, f'wyf9/home/note/cpp/{un}/')

    cmd = f'''
mkdir -p {n1d} && mkdir -p {n2d} && touch {n1} && touch {n2} && echo "# {un}-{a}. " > {n2}
'''
    print(f'run: `{cmd}`', end='')
    st = os.system(cmd)
    print(f' / stat: `{st}` /\n- {n1}\n- {n2}')


else:
    un = input('unit: ')
    while True:
        print('----------')
        a = input('Input name: ')
        n1 = os.path.join(devdir, f'.wyf9/cpp/study/{un}/{a}.cpp')
        n1d = os.path.join(devdir, f'.wyf9/cpp/study/{un}/')
        n2 = os.path.join(devdir, f'wyf9/home/note/cpp/{un}/{a}.md')
        n2d = os.path.join(devdir, f'wyf9/home/note/cpp/{un}/')

        cmd = f'''
    mkdir -p {n1d} && 
    mkdir -p {n2d} && 
    touch {n1} && 
    touch {n2} && 
    echo "# {un}-{a}. " > {n2}
    '''
        print(f'run: `{cmd}`', end='')
        st = os.system(cmd)
        print(f' / stat: `{st}` /\n- {n1}\n- {n2}')
