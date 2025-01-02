import sys
import inspect
from manim import *

class VisualCode:
    def __init__(self, func, scene):
        self.func = func
        self.scene = scene
        self.code_text, self.function_name = self.read_function_code(func)
        
        num_lines = len(self.code_text.split('\n'))
        
        self.code_mobject = Code(
            code=self.code_text,
            language="Python",
            font="Ubuntu",
            tab_width=4,
            background="rectangle",
            line_spacing=0.5,
        )

        if num_lines > 18:
            scale_factor = 18 / num_lines
            self.code_mobject.scale(scale_factor)

        self.code_mobject.to_edge(LEFT)

        self.highlight = SurroundingRectangle(
            self.code_mobject.code[0],
            color=RED,
            buff=0.0,
            stroke_width=2
        )

    def read_function_code(self, func):
        code_text = inspect.getsource(func)
        function_name = func.__name__
        return code_text, function_name

    def get_code(self):
        return self.code_mobject

    def animated_run(self, animated_list):
        self.scene.play(FadeIn(self.highlight))
        def highlight_callback(line_number):
            print(f"Highlighting line {line_number}")
            self.highlight_line(self.code_mobject, self.highlight, line_number)

        self.execute_with_trace(self.func, (animated_list,), highlight_callback)

    def highlight_line(self, code_mobject, highlight, line_number, color=RED, run_time=0.3):
        target = SurroundingRectangle(
            code_mobject.code[line_number],
            color=color,
            buff=0.0,
            stroke_width=2
        )
        target.shift(DOWN * 0.07)
        self.scene.play(Transform(highlight, target), run_time=run_time)

    def execute_with_trace(self, func, args, highlight_callback):
        def trace_calls(frame, event, arg):
            if event == 'line' and frame.f_code == func.__code__:
                func_firstlineno = func.__code__.co_firstlineno
                cur_line = frame.f_lineno - func_firstlineno
                highlight_callback(cur_line)
            return trace_calls

        sys.settrace(trace_calls)
        try:
            func(*args)
        finally:
            sys.settrace(None)
