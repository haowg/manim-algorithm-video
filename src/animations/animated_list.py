from manim import *
from ..utils.element_wrapper import ElementWrapper

class AnimatedList(list):
    """A Python list subclass that animates changes and comparisons using Manim."""
    def __init__(self, scene, *args):
        super().__init__(*args)
        self.scene = scene
        self.vgroup = VGroup(*[Text(str(item)) for item in self])
        self.highlight_color = YELLOW
        self.normal_color = WHITE
        self.message = Text("", font_size=24, color=YELLOW)
        self.vgroup.arrange(RIGHT, buff=0.5)

    def _sync_with_vgroup(self):
        """Replace old VGroup with new one to keep animations synced with list"""
        new_vgroup = VGroup(*[Text(str(item)) for item in self])
        new_vgroup.arrange(RIGHT, buff=0.5)
        self.scene.play(ReplacementTransform(self.vgroup, new_vgroup))
        self.vgroup = new_vgroup

    def append(self, item):
        super().append(item)
        new_text = Text(str(item))
        self.vgroup.add(new_text)
        self.scene.play(FadeIn(new_text))

    def remove(self, item):
        super().remove(item)
        for submob in self.vgroup:
            if submob.text == str(item):
                self.scene.play(FadeOut(submob))
                self.vgroup.remove(submob)
                break

    def pop(self, index=-1):
        item = super().pop(index)
        removed_submob = self.vgroup[index]
        self.scene.play(FadeOut(removed_submob))
        self.vgroup.remove(removed_submob)
        return item

    def extend(self, iterable):
        super().extend(iterable)
        for item in iterable:
            new_text = Text(str(item))
            self.vgroup.add(new_text)
        self.scene.play(FadeIn(self.vgroup))

    def insert(self, index, item):
        super().insert(index, item)
        self._sync_with_vgroup()

    def __getitem__(self, index):
        """Wrap the raw value in ElementWrapper for comparison animations."""
        item = super().__getitem__(index)
        return ElementWrapper(item, self, index)

    def __setitem__(self, index, value):
        """Ensure only raw values go into the list, with an update animation."""
        raw_value = value.value if isinstance(value, ElementWrapper) else value
        super().__setitem__(index, raw_value)

        old_submob = self.vgroup[index]
        new_submob = Text(str(raw_value)).set_color(YELLOW)
        new_submob.move_to(old_submob.get_center())

        # Quick highlight animations
        self.scene.play(Transform(old_submob, new_submob))
        self.vgroup[index] = new_submob

    def swap(self, i, j):
        """Swap two elements in the list with a nice animation."""
        submob1, submob2 = self.vgroup[i], self.vgroup[j]
        self.display_message(f"交换: {submob1.text} 和 {submob2.text}", [i, j])

        submob1.generate_target()
        submob2.generate_target()

        submob1.target.move_to(submob2.get_center())
        submob2.target.move_to(submob1.get_center())

        self.scene.play(MoveToTarget(submob1), MoveToTarget(submob2), run_time=0.5)
        self.vgroup[i], self.vgroup[j] = submob2, submob1
        self[i], self[j] = self[j], self[i]
        self.scene.wait(0.5)

    def compare_animation(self, i, j, relation):
        """Highlight two elements being compared"""
        submobi = self.vgroup[i]
        submobj = self.vgroup[j]
        self.display_message(f"比较: {submobi.text} 和 {submobj.text}", [i, j])
        self.scene.wait(0.3)

    def display_message(self, msg, indices=None, font_size=24, color=YELLOW):
        """Display a message and optionally highlight specific numbers."""
        new_message = Text(msg, font_size=font_size, color=color).next_to(self.vgroup, DOWN)
        self.scene.play(Transform(self.message, new_message))

        # Reset color
        for submob in self.vgroup:
            submob.set_color(WHITE)

        # Highlight specified numbers
        if indices:
            for i in indices:
                if 0 <= i < len(self.vgroup):
                    self.scene.play(self.vgroup[i].animate.set_color(YELLOW), run_time=0.01)

    def finish(self):
        """Finish the animation."""
        self.display_message("完成!!!", font_size=44, color=GREEN)
        self.scene.wait(1)
