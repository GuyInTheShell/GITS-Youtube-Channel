from manim import * # type: ignore
from numpy import array

from manim_utils import LEFT_SIDE, RIGHT_SIDE


config.background_color = "#333333"
config.frame_height = 9


class EditorTimeline(Scene):
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
