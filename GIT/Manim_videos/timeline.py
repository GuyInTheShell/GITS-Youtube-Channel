from typing import Any, Iterable, List, Optional
from manim import BLUE_D, RIGHT, UP, Animation, Line, Mobject, Scene, Circle, Create, DOWN, VMobject, np, config
from manim.animation.composition import AnimationGroup, LaggedStart
from manim.mobject.geometry.line import Arrow
from manim.mobject.text.text_mobject import Text
from manim.utils.color import RED_D, Color
from numpy import array, ndarray

from manim_utils import LEFT_SIDE, RIGHT_SIDE


config.background_color = "#333333"
config.frame_height = 9


class Timeline(Scene):
    def construct(self):
        time_width = config.frame_width - 2
        time = Arrow(start=array([LEFT_SIDE + 1, 0., 0.]), end=array([RIGHT_SIDE - 1, 0., 0.]))
        self.add(time)

        elems = [
            {"text": "Office Tools"},
            {"text": "Wiki"},
            {"text": "Collaborative Edition"},
        ]

        interval = time_width / (len(elems) + 1)
        pos = - time_width / 2 + interval
        y_dir = 1
        for elem in elems:
            event = Line(start=array([pos, 0., 0.]), end=array([pos, y_dir * 2., 0.]))
            self.play(Create(event))
            event_txt = Text(elem["text"])
            event_txt.move_to(array([pos, y_dir * 3., 0.]))
            self.play(Create(event_txt))

            self.wait()

            pos += interval
            y_dir *= -1
