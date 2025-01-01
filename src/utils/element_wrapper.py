from manim import *

class ElementWrapper:
    """Wraps a value to trigger animations on comparison."""
    def __init__(self, value, list_obj, index):
        self.value = value
        self.list_obj = list_obj
        self.index = index

    def __comparison(self, other, comp_type):
        """统一处理所有比较运算，避免重复代码。"""
        self.list_obj.compare_animation(self.index, other.index, comp_type)

    def __gt__(self, other):
        self.__comparison(other, 'gt')
        return self.value > other.value

    def __lt__(self, other):
        self.__comparison(other, 'lt')
        return self.value < other.value

    def __ge__(self, other):
        self.__comparison(other, 'ge')
        return self.value >= other.value

    def __le__(self, other):
        self.__comparison(other, 'le')
        return self.value <= other.value

    def __eq__(self, other):
        self.__comparison(other, 'eq')
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)
