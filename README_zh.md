# Manim 排序算法可视化

[English](README.md) | 简体中文

## 简介

欢迎使用 **Manim 排序算法可视化**项目！本项目使用 [Manim](https://www.manim.community/) 为各种排序算法提供动态和交互式的可视化展示。无论您是正在学习算法的学生，还是想要更好地理解排序机制的开发者，本项目都能为您提供清晰直观的排序过程演示。

## 安装

按照以下步骤设置您的环境：

### 1. 安装 Conda 和 Mamba

首先确保安装了 [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)，然后从 `conda-forge` 频道安装 `mamba`：

```bash
conda install -c conda-forge mamba
```

### 2. 创建并激活虚拟环境

为项目创建新的环境以有效管理依赖：

```bash
mamba create -n manim-env python=3.11
mamba activate manim-env
```

### 3. 安装 Manim

使用 `mamba` 从 `conda-forge` 频道安装 Manim：

```bash
mamba install -c conda-forge manim
```

### 4. 安装中文 LaTeX 支持

安装必要的 LaTeX 包以支持中文字符渲染。如果您使用的是 TeX Live，可以按如下方式安装：

```bash
sudo apt-get update
sudo apt-get install texlive-lang-chinese
```

### 5. 安装中文字体

确保系统安装了中文字体。您可以安装 Noto Sans CJK：

```bash
sudo apt-get install fonts-noto-cjk
```

### 6. 配置 Manim 中文支持

通过修改配置来使用中文字体：

```python
from manim import config

config.font = "Noto Sans CJK SC"
```

## 使用方法

1. 进入项目根目录
2. 执行 `python render.py` 渲染所有排序算法
   - 或者运行 `python render.py bubble_sort` 渲染特定排序算法

## 示例

### 冒泡排序可视化

![冒泡排序动画](media/videos/1080p60/bubble_sort.gif)

## 扩展方法

你可以通过简单地添加 `sort(arr)` 函数来创建新的排序可视化，无需创建新的场景类。

### 添加新的排序算法

只需在 `src/algorithms/sorting.py` 中添加你的排序函数即可：

```python
def your_algorithm_sort(arr):
    # 在这里实现你的排序逻辑
    # 使用 arr.swap(i, j) 来交换元素
    pass
```

注意：确保函数名以 `_sort` 结尾。

### 渲染特定排序

通过提供完整的函数名来渲染特定的排序算法：

```bash
python render.py bubble_sort insertion_sort
```

### 渲染所有排序

要自动渲染所有可用的排序算法，只需运行：

```bash
python render.py
```

这将渲染 `src.algorithms` 包中的所有排序函数。
