# Python 基本/语法

## About Python

### 语言类型

1. 编译语言: 先编译再执行
  - 运行速度快
  - 编译麻烦, 编译后的文件兼容性差
2. √脚本语言: 在执行时解释
  - 兼容性好, 可以在任何带有相同解释器的设备平台上运行
  - 速度稍慢

### Python 特点

1. 支持函数
2. 面向对象
3. 高级语言
4. 脚本语言
5. 跨平台

### 开发工具

#### 常见三方工具

1. PyCharm
  - 功能强大
  - 学习困难
2. Visual Studio Code (VSCode)
  - 多语言
3. Jupyter Notebook
  - 交互式
 
#### IDLE

1. 交互式 *(高版本默认)*
  - 即写即执行
  - 无法保存
  - 由 `>>>` 开始
  - 会显示版本等信息

| 退出方式 | Windows | MacOS |
| --- | --- | --- |
| 自带 | `File` -> `Exit IDLE` | `File` -> `Exit IDLE` |
| 命令 | `exit()` | `exit()` |
| 快捷键 | `Ctrl` + `Q` | `Command` + `Q` |
|  | `Alt` + `F4` |  |
| 关闭窗口 | 右上角 `×` | 左上角红点 |

2. 脚本式
  - 在 `.py` 文件中编写
  - 手动执行
  - 保存方便

打开方式(IDLE Shell): `Ctrl` + `N` or `File` -> `New`

运行: `Run` -> `Run Module`, 如未保存可保存

?> 后缀名: `.py`, `.pyw`, `.pyi`

## print 语句

每个 `print()` 语句输出的内容都占一行

```py
>>> print(123); print(456)
123
456
```

### 多参数输出

```py
>>> print(123, 456)
123 456 # 中间会有一个空格分隔
```

### `end` 分隔

```py
>>> print(123, end=''); print(456) # end 参数替换原本的末尾换行符
123456

>>> print(123, end='hello'); print(456) # 也可改为其他内容
123hello456

>>> print(123, end='\n'); print(456) # 换行符表示为 \n
123
456
```

### 多行输出

可以使用三个引号括起多行字符串

```py
print('''Hello
World,
UserName!''')

# ↓ 结果

Hello
World,
UserName!
```

!> 区分 多行输出(**用一个 `print()` 语句输出多行内容**) 和 单行多条语句(**在一行中执行三个独立语句**)