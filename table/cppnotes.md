# cppnotes

只是一些笔记

## 术语解释

- `include`: 包括, 包含
- `iostream`: input output stream, 输入输出流
- `using`: 使用 *(正在进行时)*
- `namespace`: 命名空间
- `std`: standard, 标准
- `int`: 整数
- `main`: 主要的, 重要的
- `cout`: console output, 控制台输出
- `endl`: end line, 结束一行
- `return`: 返回
- 编译: 将编写好的程序翻译成计算机能运行的格式

> Dev-C++ 在编写 `include` 语句时, 在输入 `<` 后会自动补全另一边的 `>`

## 示例

### 1

```cpp
#include <iostream>
using namespace std;
int main() { // main: 主函数
	cout << "Hello World!" << endl;
	return 0;
}
```