import pyxel
from pyxelext.line import poly


def update():
    pass


def draw():
    pyxel.cls(0)
    start_x = 128
    poly((start_x, 122),
         (start_x+10, 125),
         (start_x+20, 120),
         (start_x+50, 155),
         col=pyxel.frame_count % 16)


pyxel.init(256, 256, scale=2, fps=60)
pyxel.run(update, draw)
