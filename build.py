# from .note.cpp.refresh import Main as refresh
from datetime import datetime
from os import environ as env


def info(log):
    print(f'[build.py] [Info] {datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")} ' + log)


def warn(log):
    print(f'[build.py] [Warning] {datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")} ' + log)


def err(log):
    print(f'[build.py] [Error] {datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")} ' + log)

# ---------
# replace index.html


def alter(file, old_str, new_str):
    '''
    替换文件中的字符串
    :param file: 文件名
    :param old_str: 旧字符串
    :param new_str: 新字符串
    '''
    file_data = ''
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, 'w', encoding='utf-8') as f:
        f.write(file_data)


try:
    if not int(env.get('CF_PAGES')) == 1:
        err('Not CF Pages, will not replace index.html.')
    else:
        commit = env.get('CF_PAGES_COMMIT_SHA')
        alter('./index.html', '[ENV_build_full]', commit)
        alter('./index.html','[ENV_build]',commit[:7])

        info('Wrote build info into index.html ok')
except:
    err('get CF Pages env failed, will not replace index.html.')
