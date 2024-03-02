# Python Turtle库

一个进行图形绘制的标准库(*不需要额外安装*)

?> 画笔初始位置在 `(0, 0)`(中心) 处, 方向朝右

## 速查表

### 函数列表

| 名称 | 参数 | 说明 |
| --- | --- | --- |
| `forward` | (int:`length`) | 画笔前进 `length` 像素 |
| `backward` | (int:`length`) | 画笔后退 `length` 像素 |
| `setup` | [int:`x`], [int:`y`] | 打开窗口, 设置大小为 (`x`, `y`) |
|  | [float:`x`(0.xx)], [float:`y`(0.xx)] | 打开窗口, 设置大小为屏幕大小的 (`x`, `y`) |
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
| `speed` | (int:`speed`) | 设置动画速度 *(`0`: 无动画, 最快)* |
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

### 常见颜色

`red`, `green`, `blue`, `yellow`, `orange`, `pink`, `purple`, `black`, `white`

> 也可使用 RGB 来表示颜色

## Tips

### 正多边形旋转角度

正 `n` 边形:

外角角度 = 360° / `n`