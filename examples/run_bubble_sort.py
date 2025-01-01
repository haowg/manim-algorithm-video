import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manim import config
from src.algorithms.bubble_sort import BubbleSortScene

if __name__ == "__main__":
    config.verbosity = "WARNING"
    config.preview = True
    scene = BubbleSortScene()
    scene.render()
