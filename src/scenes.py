from manim import *
from .animations.animated_list import AnimatedList
from .utils.visual_code import VisualCode

class GenericSortScene(Scene):
    def __init__(self, sort_func, *args, **kwargs):
        self.sort_func = sort_func
        # Add scene name based on sort function
        self.name = sort_func.__name__
        super().__init__(*args, **kwargs)

    def construct(self):
        visual_code = VisualCode(self.sort_func, self)
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
