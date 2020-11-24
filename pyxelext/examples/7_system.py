import pyxel
from pyxelext.system import *


def update():
    if pyxel.btn(pyxel.KEY_F):
        set_fullscreen()

    if pyxel.btn(pyxel.KEY_W):
        set_windowed()


def draw():
    pyxel.cls(0)
    pyxel.text(100, 50, f'Toggle Fullscreen with W and F key', pyxel.COLOR_WHITE)
    pyxel.text(100, 100, f'Pyxel is in fullscreen: {pyxel.is_fullscreen}', pyxel.COLOR_WHITE)


pyxel.init(256, 256, scale=2)
set_window_icon('images/test.ico')

pyxel.run(update, draw)
