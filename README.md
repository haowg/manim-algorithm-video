# manim-sorting-visualizations

## Introduction

Welcome to the **Manim Sorting Visualizations** project! This repository provides dynamic and interactive visualizations of various sorting algorithms using [Manim](https://www.manim.community/). Whether you're a student learning algorithms or a developer looking to understand sorting mechanisms better, this project offers clear and animated demonstrations of sorting processes.

## Installation

To get started with the project, follow these steps to set up your environment:

### 1. Install Conda and Mamba

First, ensure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed. Then, install `mamba`, a fast `Conda` alternative, from the `conda-forge` channel:

```bash
conda install -c conda-forge mamba
```

### 2. Create and Activate a Virtual Environment

Create a new environment for the project to manage dependencies effectively:

```bash
mamba create -n manim-env python=3.11
mamba activate manim-env
```

### 3. Install Manim

Install Manim from the `conda-forge` channel using `mamba`:

```bash
mamba install -c conda-forge manim
```

### 4. Install Chinese LaTeX Support

To render Chinese characters in LaTeX, install the necessary LaTeX packages. If you're using TeX Live, you can install the required packages as follows:

```bash
sudo apt-get update
sudo apt-get install texlive-lang-chinese
```

Alternatively, if you're using a different LaTeX distribution, refer to its documentation for installing Chinese language support.

### 5. Install Chinese Fonts

Ensure that you have Chinese fonts installed on your system. You can install popular Chinese fonts like Noto Sans CJK:

```bash
sudo apt-get install fonts-noto-cjk
```

### 6. Configure Manim for Chinese Support

Update your Manim configuration to use Chinese fonts. You can do this by modifying the `config` in your scripts or by setting it globally.

Example configuration in your Python script:

```python
from manim import config

config.font = "Noto Sans CJK SC"
```

## How to Run

1. Navigate to the project's root directory.
2. Execute `python render.py` to render all sorting algorithms at once.
   - Alternatively, run `python render.py bubble_sort` to render a specific sort.

## Examples

### Bubble Sort Visualization

![Bubble Sort Animation](media/videos/1080p60/bubble_sort.gif)

## Enhanced Run Method

You can now add new sorting visualizations by simply adding a `sort(arr)` function without creating a new Scene class.

### Add a New Sorting Algorithm

Simply add your sorting function to `src/algorithms/sorting.py`. For example:

```python
def your_algorithm_sort(arr):
    # Implement your sorting logic here
    # Use arr.swap(i, j) to swap elements
    pass
```

Note: Make sure your function name ends with `_sort`.

### Render Specific Sorts

To render specific sorting algorithms, provide the fully qualified function names as arguments:

```bash
python render.py bubble_sort insertion_sort
```

### Render All Sorts

To render all available sorting algorithms automatically, simply run:

```bash
python render.py
```

This will discover and render all `sort` functions within the `src.algorithms` package.

