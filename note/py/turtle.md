# Python Turtle库

一个进行图形绘制的标准库(*《不 需 要 额 外 安 装》* -> 仅指某学习客户端自带的环境中)

?> 画笔初始位置在 `(0, 0)`(中心) 处, 方向朝右

## 速查表

### 函数列表

(`turtle.`)

| 名称 | 参数 | 说明 |
| --- | --- | --- |
| `forward` | (int:`length`) | 画笔前进 `length` 像素 |
| `backward` | (int:`length`) | 画笔后退 `length` 像素 |
| `setup` | [int:`x`], [int:`y`] | 打开窗口, 设置大小为 (`x`, `y`) |
|  | [float:`x`], [float:`y`] | 打开窗口, 设置大小为屏幕大小的 (`x`, `y`) **(`<= 1.0` 的小数)** |
|  | [int:`x`], [int:`y`], [int:`sx`], [int:`sy`] | 打开窗口, 设置大小为 (`x`, `y`), 窗口位置为 (`sx`, `sy`) |
| `screensize` | (int:`x`), (int:`y`), [str:`color`] | 设置窗口的大小为 (`x`, `y`), 并设置背景颜色为 `color` |
| `done` |  | 结束绘画，并**保留窗口(必备)** |
| `goto` | (int:`x`), (int:`y`) | 画笔平移到 (`x`, `y`) |
| `reset` |  | 重置画布, **画笔变为初始状态** |
| `clear` |  | 清除画布, **画笔状态不变** |
| `home` |  | 画笔平移到 (`0`, `0`), **并恢复朝向** |
| `penup` |  | 切换为抬笔状态 |
| `pendown` |  | 切换为落笔状态 *(默认)* |
| `showturtle` |  | 显示画笔 *(默认)* |
| `hideturtle` |  | 隐藏画笔 |
| `speed` | (int:`speed`) | 设置动画速度 (`speed` 取值: `0` ~ `10`) *(`0`: 无动画, 最快)* |
| `shape` | (str:`shape`) | 设置画笔形状, 可选: ('`turtle`'*(海龟)* / '`arrow`'*(箭头, 默认)* / '`circle`'*(圆形)*) |
| `pensize` | (int:`size`) | 设置画笔粗细(宽度) *(像素)* |
| `pencolor` | (str:`color`) | 修改画笔颜色为 `color` |
| `fillcolor` | (str:`color`) | 修改填充颜色为 `color` |
| `color` | (str:`pcolor`), (str:`fcolor`) | 设置画笔颜色为 `pcolor`, 填充颜色为 `fcolor` |
|  | (str:`color`) | 设置画笔/填充颜色都为 `color` |
| `bgcolor` | (str:`color`) | 修改背景颜色为 `color` |
| `begin_fill` |  | 开始填充 |
| `end_fill` |  | 结束填充 |
| `dot` | [`d`], (str:`color`) | 画 **直径**为 `d` 像素, `color` 色的原点 (默认直径: [`pensize+4` / `2*pensize` *(取最大)*]) |
| `circle` | (int:`r`), [int:`o`], [int:`n`] | 半径为 `r`, 度数为 `o` *(默认: 360)* , 边数为 `n` 的正多边形 **(`r` ≠ 边长)** |
|  | (`r`), [`steps`=`n`] | 画半径为 `r`, 边数为 `n` 的正多边形 **(`r` ≠ 边长)** |
| `listen` |  | 开始监听点击 / 按键等事件 **(执行后才能使 `onscreenclick` 和 `onkeypress` 类函数生效)** |
| `onscreenclick` | (func:`function`) | 在鼠标点击屏幕时调用 `function` 函数并传参 (`x`, `y`), *如: `turtle.onscreenclick(turtle.goto)`* |
| `onkeypress` | (func:`function`), (str:`key`) | 在 `key` 键被按下时执行 `function` 函数 |
| `tracer` | (bool: `True` / `False`) | 设置追踪(即True时自动追踪更改显示, False时不追踪更改, 需要使用 `update` 来显示) |
| `update` |  | 更新画面(一般在 `tracer(False)` 时使用) |
| `write` | (str: `text`), [tuple: font (str: `name`, int: `size`, str: `type`)] | 直接显示文字 ([参数说明](#write)) |
| `setheading` | (int:`to_angle`) | 将画笔朝向角度设为 `to_angle` *(正右边为 `0`, 逆时针增加)* |
| `heading` |  | 获取画笔朝向角度 |

### 状态获取

(`turtle.`)

| 名称 | 参数 | 说明 |
| --- | --- | --- |
| `heading()` |  | 目前的画笔方向 (`0` ~ `359`), **注意: 返回的是小数, 如 `30.0`**|

?> 这类获取信息的函数用 `return` 返回数据, 一般需要使用变量存储或进行其他操作, 如:

```py
angle = turtle.heading() # 存储至 `angle`
print(turtle.heading()) # 直接打印
# output: 30.0
```


#### write

示例: `turtle.write('text', font = ('space mono', 20, 'bold'))`

`text`: 要显示的文本

- 常见: `space mono`, `menlo`, `consolas`
`space mono`: 字体
`20`: 字号(即字的大小, 与其成正比)
`bold`: 属性: `normal`(正常), `bold`(加粗), `italic`(倾斜)

!> 注意 `font` 定义顺序

> 可用画笔颜色来控制输出文本的颜色

### `Turtle` 对象

借助 `Turtle` 对象可以实现类似"分身"的效果(即`clear()`等操作都不会影响另一个)

```py
# 创建
name = turtle.Turtle() # 初始化对象

# 接下来就可以和一般的 `turtle` 一样使用了
name.circle(100)
```


### 常见颜色

`red`, `green`, `blue`, `yellow`, `orange`, `pink`, `purple`, `black`, `white`

> 也可使用 RGB 来表示颜色

## Tips

### 正多边形旋转角度

正 `n` 边形:

外角角度 = 360° / `n`