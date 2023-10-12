from manim import config

TOP = 0
BOTTOM = 0
LEFT_SIDE = 0
RIGHT_SIDE = 0

def compute_helper_constants():
    global TOP, BOTTOM, RIGHT_SIDE, LEFT_SIDE

    TOP = config.frame_height / 2
    BOTTOM = -1 * TOP

    RIGHT_SIDE = config.frame_width / 2
    LEFT_SIDE = -1 * RIGHT_SIDE

compute_helper_constants()
