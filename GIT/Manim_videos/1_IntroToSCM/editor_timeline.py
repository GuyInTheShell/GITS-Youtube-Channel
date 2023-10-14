from pathlib import Path

from manim import ORIGIN, Arrow, Create, FadeIn, ImageMobject, Line, Scene, Text, config
from numpy import array

from manim_utils import H_UNIT, LEFT_SIDE, PALETTES, RIGHT_SIDE, V_UNIT

PALETTE = PALETTES["BlackGrayYellowNightGradient"]

config.background_color = PALETTE[0]
config.frame_height = 9

TEXT_COLOR = PALETTE[3]

SCENE_DIR = Path(__file__).parent.absolute()
RESOURCES_DIR = SCENE_DIR.joinpath("resources")


class EditorTimeline(Scene):
    def construct(self):
        time_width = config.frame_width - 2
        time = Arrow(start=array([LEFT_SIDE + 1, 0., 0.]), end=array([RIGHT_SIDE - 1, 0., 0.]), color=TEXT_COLOR)
        self.add(time)

        elems = [
            {"text": "Office Tools", "images": ["ppt.png", "xls.png", "doc.png"]},
            {"text": "Wiki", "images": ["Wikipedia.png"]},
            {"text": "Collaborative Edition", "images": ["CollaborativeEditing.png"]},
        ]

        interval = time_width / (len(elems) + 1)
        pos = - time_width / 2 + interval
        y_dir = 1
        for elem in elems:
            event = Line(start=array([pos, 0., 0.]), end=array([pos, y_dir * V_UNIT, 0.]))
            self.play(Create(event))
            event_txt = Text(elem["text"], color=TEXT_COLOR)
            event_txt.move_to(array([pos, y_dir * 2 * V_UNIT, 0.]))

            imgs = []
            h_offset = - (len(elem["images"]) // 2) * 0.5 * H_UNIT
            v_offset = 0
            for img in elem["images"]:
                image = ImageMobject(RESOURCES_DIR.joinpath(img))
                image.height = 1 * V_UNIT
                image.move_to(array([pos + h_offset, y_dir * 3 * V_UNIT + v_offset * 0.3 * V_UNIT, 0.]), ORIGIN)
                imgs.append(image)

                h_offset += 0.5 * H_UNIT
                v_offset += 0.5 * V_UNIT

            self.play(Create(event_txt))
            for image in imgs:
                self.play(FadeIn(image))

            self.wait()

            pos += interval
            y_dir *= -1
