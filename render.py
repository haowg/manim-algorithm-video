import os
import sys
import argparse
import importlib
import pkgutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from manim import config
from src.algorithms.sorting import *
from src.scenes import GenericSortScene

def discover_sort_functions(package):
    """Find all sort functions in sorting.py"""
    sort_functions = []
    module = sys.modules['src.algorithms.sorting']
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if callable(attribute) and attribute.__name__.endswith('_sort'):
            sort_functions.append(attribute)
    return sort_functions

def short_name_to_full_path(name, discovered):
    """Convert sort name to full module path if it exists in discovered functions"""
    for func in discovered:
        if func.__name__ == name:
            return f"{func.__module__}.{func.__name__}"
    return None

def main():
    config.verbosity = "WARNING"
    config.preview = True

    all_sorts = discover_sort_functions("src.algorithms")
    sort_choices = [func.__name__ for func in all_sorts]

    parser = argparse.ArgumentParser(description="Render Manim sorting visualizations.")
    parser.add_argument(
        'sorts',
        metavar='S',
        type=str,
        nargs='*',
        help='Sorting algorithms you want to render (e.g. bubble_sort, insertion_sort, or "all").'
    )
    args = parser.parse_args()

    if 'all' in args.sorts:
        print("Rendering all available sorts.")
        for sort_func in all_sorts:
            config.output_file = sort_func.__name__
            scene = GenericSortScene(sort_func)
            scene.render()
            config.output_file = None
        return

    if not args.sorts:
        print("No sorting algorithm specified.\nAvailable sorts:")
        for s in sort_choices:
            print(f"  {s}")
        print('\nUse "python render.py all" to render all sorts, or specify sorts like "python render.py bubble_sort"')
        return

    for short_name in args.sorts:
        full_path = short_name_to_full_path(short_name, all_sorts)
        if not full_path:
            print(f"Unknown sort: {short_name}. Available sorts:")
            for s in sort_choices:
                print(f"  {s}")
            continue
        module_path, func_name = full_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        sort_func = getattr(module, func_name)
        config.output_file = sort_func.__name__
        scene = GenericSortScene(sort_func)
        scene.render()
        config.output_file = None

if __name__ == "__main__":
    main()