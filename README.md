# Flow Network

网络流的工业级应用

![Release Drafter](https://github.com/LucienShui/flow-network/workflows/Release%20Drafter/badge.svg)
![Upload Python Package](https://github.com/LucienShui/flow-network/workflows/Upload%20Python%20Package/badge.svg)

使用 `Dinic` 和朴素费用流，算法来自 [DuckKnowNothing - 网络流](https://github.com/UPCACM/DuckKnowNothing/tree/master/src/GraphAlgorithm/%E7%BD%91%E7%BB%9C%E6%B5%81) 

## 支持平台

> 在尝试了各种方法之后，GitHub Actions 在 Windows 平台下始终无法正确编译 C++，所以放弃支持 Windows 平台

+ Linux
+ macOS

## 安装

```bash
pip install flow-network
```

## 样例代码

```python
from flow_network import MaximumFlow, MinimumCostFlow

mf = MaximumFlow(2)  # 创建一个包含 2 个点的网络流对象，下标从 0 开始
mf.add_edge(0, 1, 3)  # 添加一条从 0 指向 1 的边，流量为 3
result = mf.run(0, 1)  # 指定源点为 0，汇点为 1，跑最大流 & 最小割
print(result)  # 3

mcf = MinimumCostFlow(2)  # 创建一个包含 2 个点的费用流对象，下标从 1 开始
mcf.add_edge(0, 1, 3, 2)  # 添加一条从 0 指向 1 的边，流量为 3，单位流量的费用为 2
flow, cost = mcf.run(0, 1)  # 指定源点为 0，汇点为 1，跑最大流 & 最小费
print(flow, cost)  # 3 6
```

### 测试代码

[tests.py](https://github.com/LucienShui/flow-network/blob/main/tests.py)

## Reference

+ [How to use C++ classes with ctypes?](https://stackoverflow.com/questions/1615813/how-to-use-c-classes-with-ctypes)
+ [Calling C/C++ from Python?](https://stackoverflow.com/questions/145270/calling-c-c-from-python)
+ [C Class Instance from Void Pointer using Ctypes](https://stackoverflow.com/questions/19389124/c-class-instance-from-void-pointer-using-ctypes)
+ [Python 库打包分发、setup.py 编写、混合 C 扩展打包的简易指南（转载）](https://www.cnblogs.com/xueweihan/p/12030457.html)
+ [Binary wheel can't be uploaded on pypi using twine](https://stackoverflow.com/questions/59451069/binary-wheel-cant-be-uploaded-on-pypi-using-twine)
+ [Manylinux wheel builder](https://github.com/Niraj-Kamdar/manylinux-wheel-builder)
