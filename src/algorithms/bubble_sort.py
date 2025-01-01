from manim import *
from ..animations.animated_list import AnimatedList
from ..utils.visual_code import VisualCode

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr.swap(j, j + 1)

class BubbleSortScene(Scene):
    def construct(self):
        visual_code = VisualCode(bubble_sort, self)
        code_mobject = visual_code.get_code()
        self.play(FadeIn(code_mobject))

        a_list = AnimatedList(self, [10, 2, 1])
        a_list.vgroup.next_to(code_mobject, RIGHT, buff=1)
        self.add(a_list.vgroup)
        a_list.message.next_to(a_list.vgroup, DOWN)

        self.wait(1)
        visual_code.animated_run(a_list)
        a_list.finish()
        self.wait(3)
