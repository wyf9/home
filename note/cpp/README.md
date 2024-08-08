### README

在课上整理的 C++ 笔记库

### Tips

!> 可用短链快速打开: https://wyf9.top/t/cpp

?> 如初次学习需要参考, 可[快速开始](quickstart.md) / 也可以作为速查笔记来使用

?> 可通过左下角 `≡` *(三个杠)* 符号呼出/收起侧边栏，在侧边栏中查看目录

> [查看目录文件 `_sidebar.md`](./_sidebar.md)

?> `*` 代表笔记未完成, `^` 代表未做

<!--
no test:
2-10 to 2-24
3-1 to 3-6

undone:
3-7 to ...

(include)
-->

---

### **阅前必读**

#### 1. 关于文章格式

文中的代码块一般有两种类型: `cpp` 或 `output`

1. `cpp`

即 C++ 源代码

- 一个 `cpp` 代码块中如果有如 `int main()` 及 `#include` 一类语句，则表明这**是完整的代码**，可以直接拿来编译运行

- 否则则**不是**，需要补全基本函数，头文件等才可运行

> 需要的头文件可能会有提示，也可在完整示例中寻找

2. `output`

中文意思 **"输出"**，顾名思义，用于程序的运行结果

每一行会有以下三种符号：

- `< `: 表示后面的内容为用户的输入
- `> `: 表示后面的内容为程序的输出
- `- `: 表示后面的内容与程序无关 *(如 shell)*

#### 2. ProblemID

带有 `ProblemID` 的题目代表存在于 OJ 系统中，可用下面的链接打开:

```
http://oj.xw3q.cn:9905/problem.php?id=<id>
```

> 将 `<id>` 替换为 ProblemID

<div id="copy-3-id"><a href="javascript:copym('http://oj.xw3q.cn:9905/problem.php?id=', 'copy-3-id', '复制成功', 1000)">点击复制</a> <code>id</code> 前的部分</div>

> or:

<!-- script is in index: #1 p_note_cpp_readme_jump() -->

<input type="number" id="inputBox" name="inputBox" placeholder="ProblemID">
<button onclick="p_note_cpp_readme_jump()">跳转</button>

---

### Useful

##### 题解模板

<div id="copy-1"><a href="javascript:copym('**ProblemID**: ``\n\n**程序名**: \n\n**题目描述**: \n\n**输入**: \n\n**输出**: \n\n**样例输入**:\n```text\n\n```\n\n**样例输出**:\n```text\n\n```', 'copy-1', '复制成功', 1000)">点击复制</a></div>

<div id="copy-2"><a href="javascript:copym('**程序名**: \n\n**题目描述**: \n\n**输入**: \n\n**输出**: \n\n**样例输入**:\n```text\n\n```\n\n**样例输出**:\n```text\n\n```', 'copy-2', '复制成功', 1000)">点击复制 (Without ProblemID)</a></div>

!> 请直接使用上面的按钮复制即可忽略 `\`

<details>
<summary>Show</summary>

```md
**ProblemID**: ``

**程序名**: 

**题目描述**: 

**输入**: 

**输出**: 

**样例输入**:

\`\`\`text

\`\`\`

**样例输出**:

\`\`\`text

\`\`\`

```

</details>

##### 解题模板

```cpp
#include <iostream>
using namespace std;
int main() {
    // 1. 定义变量

    // 2. 输入数据

    // 3. 计算或处理数据

    // 4. 输出结果

    return 0;
}
```

##### 点击展开

```md
<details>
<summary>点击展开</summary>
此处为内容
</details>
```

<details>
<summary>点击展开</summary>
此处为内容
</details>