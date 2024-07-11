# #coding:utf-8
print('在使用前，请确保目标文件末尾(只)有一个空行')
unit = input('I/unit: ')
start = int(input('I/start: '))
end = int(input('I/end: '))
for i in range(start, end+1):
    t = input(f'({start}/{i}/{end}) title: ')
    content = f'  - [^{unit}-{i}. {t}]({unit}/{i}.md)\n'
    content_s = f'  - [^{unit}-{i}. {t}](../{unit}/{i}.md)\n'
    with open('_sidebar.md', 'a+') as f:
        f.write(content)
    with open('_sidebar_sub.md', 'a+') as f:
        f.write(content_s)

    #  - [^2-14. 求绝对值](2/14.md)
    #  - [1-37. 交换数值](../1/37.md)

if input('Refresh now? (y/...): ') == 'y':
    from refresh import Main
    Main()