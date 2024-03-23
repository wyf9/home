# 数据类型

## 变量

?> 保存程序中的临时数据

```py
a        =          3

变量名   赋值符号   值
```

### 变量名

?> 可使用: 字母, 数字, 下划线, 中文 **(不推荐)**

1. 不能用**数字**作**开头**
2. 不能使用除 `_` *(下划线)* 以外的**符号**
3. 不能使用**保留字**

Example:

```py
>>> lang = 'python' # 纯字母 √√√
>>> lang1 = 'python' # 带数字 (非开头) √
>>> _lang = 'python' # 带下划线 √
>>> 语言 = 'python' # 带中文 √

>>> .lang = 'python
  File "<stdin>", line 1
    .lang = 'python
    ^
SyntaxError: invalid syntax # 不能使用特殊符号 ×

>>> 1lang = 'python'
  File "<stdin>", line 1
    1lang = 'python'
    ^
SyntaxError: invalid decimal literal # 不能使用数字(开头) ×

>>> True = 'python'
  File "<stdin>", line 1
    True = 'python'
    ^^^^
SyntaxError: cannot assign to True # 不能使用保留字 True ×

>>> if = 'python'
  File "<stdin>", line 1
    if = 'python'
       ^
SyntaxError: invalid syntax # 不能使用保留字 if ×
```

#### 保留字 / 关键字

可通过如下 Python 命令查看:

```py
import keyword
print(keyword.kwlist)
```

```py
# Python 3.11.7 (main, Dec  8 2023, 18:56:58) [GCC 11.4.0] on linux
['False', 'None', 'True', 'and', 'as',
'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
```

#### **大小写敏感**

Example:

```py
>>> A = 3 # 为 A 赋值
>>> print(a) # 输出 a 的值
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined. Did you mean: 'A'? # 原因: A ≠ a
```

### 赋值符号

[Here](/table/py/calc?id=赋值运算)

### 多句代码

```py
a = 1
b = 2
```

等同于:

```py
a = 1; b = 2
```

## 数据类型

1. `str` (字符串): `'abc'`

数字类:

2. `int` (整数): `123`
3. `float` (浮点): `123.456`
4. `bool` **(布尔)**: `True` or `False`
5. `complex` *(复数)*

集合类:

6. `list` (列表): `[a, b, c]`
7. `tuple` (元组): `(a, b, c)`
8. `set` (集合)
9. `dict` (字典): `{'a': d, 'b': e, 'c': f}`

其他:

10. *`None` (无)*

### 查看类型

`type <s数据>`

```py
>>> type('hello')
<class 'str'>
>>> type(123)
<class 'int'>
>>> type(45.6)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type((1, 2, 3))
<class 'tuple'>
>>> type([1, 2, 3])
<class 'list'>
>>> type({'a': 1, 'b': 2, 'c': 3})
<class 'dict'>
```

### 注意

!> 字符串的引号不能混用，如:

```py
>>> test = 'hello"
  File "<stdin>", line 1
    test = 'hello"
           ^
SyntaxError: unterminated string literal (detected at line 1) # 混用

>>> test2 = 'hello' # 单引号
>>> test3 = "hello" # 双引号

```

### 字符串运算

1. `+` (拼接): `'1' + '2'` = `'12'`
2. `*` (重复): `'123' * 2` = `'123123'`

> 先**重复**后**拼接**

!> 只能拼接**字符串和字符串**, 如:

```py
>>> 'a' + 'b' # 字符串 + 字符串
'ab'
>>> 'abc' + 123 # 字符串 + 数字
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

## 类型转换

1. 整型: `int`(`str` / `float`)

```python
>>> int(9.7)
9 # 浮点数转换为整数时, 将舍弃小数部分
>>> int('5')
5 # 整数字符串 √
>>> int('8.8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '8.8' # 小数字符串 ×
```

2. 浮点型: `float`(`str` / `int`)

```py
>>> float(6)
6.0 # 加上小数点
>>> float('5')
5.0 # 整数字符串 √
>>> float('8.8')
8.8 # 小数字符串 √
```

3. 字符串: `str`(...)

```py
>>> str(5) # int
'5'
>>> str(7.9) # float
'7.9'
>>> str(True) # bool
'True'
```

4. 表达式: `eval`(`str`)

```py
>>> eval('5+4'), type(eval('5+4'))
(9, <class 'int'>)
>>> eval('9/2'), type(eval('9/2'))
(4.5, <class 'float'>)
>>> eval('True'), type(eval('True'))
(True, <class 'bool'>)

>>> a = 1.27
>>> eval('a+10'), type(eval('a+10'))
(11.27, <class 'float'>)
```