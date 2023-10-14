from manim import config

PALETTES = {
    # https://colorhunt.co/palette/27282961677ad8d9dafff6e0
    "BlackGrayYellowNightGradient": ["#272829", "#61677A", "#D8D9DA", "#FFF6E0"],
    # https://colorhunt.co/palette/2c3333395b64a5c9cae7f6f2
    "DarkBlackNavyTealColdNightGradientSea": ["#2C3333", "#395B64", "#A5C9CA", "#E7F6F2"],
}

H_UNIT = config.frame_width / 16 / 2
V_UNIT = config.frame_width / 9 / 2

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
