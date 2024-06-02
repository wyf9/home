# QuickStart - 快速开始

请从下面选择你使用的平台, 开始教程↓↓↓

<!-- tabs:start -->

#### **Windows**

1. 下载 `Dev-Cpp` 软件并安装

?> 作者官网下载: [devcpp.gitee.io](https://devcpp.gitee.io/)

<!--
下面为旧版本 `5.16i`

64 位系统: [Here](https://alist.wyf9.top/alidrive/dl/programs/devcpp/Dev-Cpp-5.16i-x64.exe)

32 位系统: 请 [自行寻找其他版本](https://cn.bing.com/search?q=dev+cpp+32%E4%BD%8D%E5%AE%89%E8%A3%85)
-->

2. (可选)进行基本配置

#### **Linux**

?> 以下使用 `Ubuntu` 系统演示, 其他分支可参考或 [自行搜索](https://cn.bing.com/search?q=linux%E6%90%AD%E5%BB%BAc%2B%2B%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83)

##### 安装

只需要安装 `g++` 和 `make` 两个软件包即可

```shell
sudo apt update
sudo apt install g++ make
```

##### 使用

```shell
g++ -o <程序名> <源代码文件>
```

如:

```shell
g++ -o myprogram mycode.cpp
```

即使用 `mycode.cpp` 文件编译出可执行文件 `myprogram`

#### **MacOS**

不提供教程, 请 [自行搜索](https://cn.bing.com/search?q=macos%E6%90%AD%E5%BB%BAc%2B%2B%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83)

<!-- tabs:end -->

> -> [1. 第一个 C++ 程序](1-1.md)