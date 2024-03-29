# Python 运算符

## 数字

1. 整数型 (`1`)
2. 浮点型 (`1.0`)

!> 1. 除法 *(`/`)* 运算为**浮点运算**, 即 `30 / 5` = `6.0`

!> 2. **浮点和任何数字运算都为浮点型**, 即 `3.0 * 5` = `15.0`

!> 3. 与数学运算顺序相同, 即**先括号, 后乘除, 最后加减**

## 基本符号

运算: `+`, `-`, `*`, `/`, `%`, `//`, `**`

### 取余 - `%`

Example:

1. 7/2=3...1 -> `7 % 2` = `1`
2. 10/5=2(...0) -> `10 % 5` = `0`

### 取整除 - `//`

> 注意: **不会四舍五入**

Example:

1. 78/10=7.8 -> `78 // 10` = 7
2. 23/10=2.3 -> `23 // 10` = 2

### 幂运算 - `**`

> 即为乘方运算

Example:

1. `2 ** 4` -> `2 * 2 * 2 * 2` (`2^4`) = `16`
2. `4 ** 3` -> `4 * 4 * 4` (`4^3`) = `64`

## 赋值运算

### > `=`

1. 普通赋值: `a = 1`
2. 赋不同值: `a, b, c = 5, 10, 15` -> `a = 5`, `b = 10`, `c = 15`
3. 赋相同值: `a = b = c = 10` -> `a = 10`, `b = 10`, `c = 10`
4. 交换赋值: `a, b = b, a`: `a = 1`, `b = 2` -> `a = 2`, `b = 1`

### > `+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=`

?> 如: `a += 5` -> `a = a + 5`

| 原运算 | 化简运算 |
| --- | --- |
| `a = a + 5` | `a += 5` |
| `a = a - 5` | `a -= 5` |
| `a = a * 5` | `a *= 5` |
| `a = a / 5` | `a /= 5` |
| `a = a % 5` | `a %= 5` |
| `a = a // 5` | `a //= 5` |
| `a = a ** 5` | `a **= 5` |

### 基本运算符优先级

(**优先级小的先算**)

> 从上到下递减, 同级运算**从左往右**

| 运算符 | 说明 | 优先级 |
| --- | --- | --- |
| `()` | 小括号 | 19 |
| `**` | 幂 (乘方) | 16 |
| `*` | 乘 | 13 |
| `/` | 除 | 13 |
| `%` | 取余 | 13 |
| `//` | 取整除 | 13 |
| `+` | 加 | 12 |
| `-` | 减 | 12 |

顺序: `()`  >  `**`  >  `*`, `/`, `%`, `//`  >  `+`, `-`

## 比较运算符

`>`, `<`, `==`, `!=` `>=`, `<=` -> `True` or `False`

| 符号 | 名称 | 说明 |
| --- | --- | --- |
| `>` | 大于 |  |
| `<` | 小于 |  |
| `==` | 等于 | **有两个等号** |
| `!=` | 不等于 |  |
| `>=` | 大于等于 | 即 ≥ , `>` or `=` |
| `<=` | 小于等于 | 即 ≤ , `<` or `=` |

### 布尔值和数字的比较

**布尔值属于数字**, 值相等情况下 `int` == `float`
1. **`0` == `False`**
2. **`1` == `True`**
3. **`10` == `10.0`**

### 字符串比较

Example:

(1) `'122' > '13'` -> `False`

顺序:123------12

1. 比较第一位, `1` = `1`
2. 比较第二位, `2` < `3` -> `<`

**几位相同的情况下, 长度长的更大**

### 单个字母比较

按照 ASCII 码表对应数字比较:

| 大写字符 | 十进制 | 小写字符 | 十进制 |
| -------- | ------ | -------- | ------ |
| A        | 65     | a        | 97     |
| B        | 66     | b        | 98     |
| C        | 67     | c        | 99     |
| D        | 68     | d        | 100    |
| E        | 69     | e        | 101    |
| F        | 70     | f        | 102    |
| G        | 71     | g        | 103    |
| H        | 72     | h        | 104    |
| I        | 73     | i        | 105    |
| J        | 74     | j        | 106    |
| K        | 75     | k        | 107    |
| L        | 76     | l        | 108    |
| M        | 77     | m        | 109    |
| N        | 78     | n        | 110    |
| O        | 79     | o        | 111    |
| P        | 80     | p        | 112    |
| Q        | 81     | q        | 113    |
| R        | 82     | r        | 114    |
| S        | 83     | s        | 115    |
| T        | 84     | t        | 116    |
| U        | 85     | u        | 117    |
| V        | 86     | v        | 118    |
| W        | 87     | w        | 119    |
| X        | 88     | x        | 120    |
| Y        | 89     | y        | 121    |
| Z        | 90     | z        | 122    |

> 大写字母: `64` + 字母表顺序

> 小写字母: `96` + 字母表顺序

字母顺序决定大小, 小写字母 > 大写字母

Example:

1. 'aa' > 'ab' -> `False`

    12----12

- ①`a == a`, ②`a < b`

2. `abcd` > `abb` -> `True`

    1234-----123

- ①`a == a`, ②`b = b`, ③`c > b`

## 逻辑运算符

与: `and`, 或: `or`, `not`

1. `True` and `True` -> `True`
2. `True` and `False` -> `False`
3. `False` and `False` -> `False`

4. `True` or `True` -> `True`
5. `True` or `False` -> `True`
6. `False` or `False` -> `False`

`not True` -> `False`
`not False` -> `True`

> 先比较后进行逻辑运算

### 数字作判断条件

!> `0` -> `False`, 其他数字均为 `True`

#### > `or`

遇到 `True` 返回, 否则返回最后一个

1. `1 or 2` -> `1`:
  - `1` -> `True`, 即返回 `1`
2. `0 or -5` -> `-5`:
  - `0` -> `False`,
  - `-5` -> `True`, 即返回 `-5`
3. `False or 0` -> `0`:
  - `False`,
  - `0` -> `False`, 即返回 `0`

#### > `and`

遇到 `False` 返回, 否则返回最后一个

1. `1 and 2` -> `2`
  - `1` -> `True`,
  - `2` -> `True`, 即返回 `2`
2. `0 and 2` -> `0`
  - `0` -> `False`, 即返回 `0`

## 运算优先级

(**优先级`数字`小的先算**)

| 名称 | 例 | 优先级 |
| --- | --- | --- |
| 算数运算 | `1 + 1` | 1 |
| 比较运算 | `2 > 1` | 2 |
| 逻辑运算 | `True or False` | 2 |

顺序: 算数运算 -> 比较运算 -> 逻辑运算

| 逻辑运算符 | 优先级 |
| --- | --- |
| `not` | 1 |
| `and` | 2 |
| `or` | 3 |

顺序: `not` -> `and` -> `or`