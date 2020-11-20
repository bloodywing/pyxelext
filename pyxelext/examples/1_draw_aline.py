import pyxel
from pyxelext.line import aline

a1 = 0
a2 = 0


def update():
    pass


def draw():
    global a1, a2
    pyxel.cls(0)
    for r in range(0, 360, 10):
        aline(50, 50, 20, pyxel.COLOR_WHITE, r)

    for r in range(0, pyxel.width, 10):
        aline(r, 160, pyxel.frame_count % 50, pyxel.COLOR_CYAN, -45)

    aline(128, 60, 50, pyxel.COLOR_GREEN, a1)
    aline(128, 60, 50, pyxel.COLOR_RED, a2)

    a1 += 1
    a2 -= 5


pyxel.init(256, 256, scale=2, fps=60)
pyxel.run(update, draw)
