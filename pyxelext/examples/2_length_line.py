import pyxel
from pyxelext.line import line


def update():
    pass


def draw():
    pyxel.cls(0)
    v = pyxel.frame_count % 30 + 10
    length = line(10, 10, v, 10, pyxel.COLOR_WHITE)
    length2 = line(10 + length, 10, v*2 + length, 10, pyxel.COLOR_RED)
    pyxel.text(10, 60, f'Line has a length of {length} PX', pyxel.COLOR_GREEN)
    pyxel.text(10, 70, f'Line 2 has a length of {length2} PX', pyxel.COLOR_GREEN)


pyxel.init(256, 256, scale=2, fps=10)
pyxel.run(update, draw)
