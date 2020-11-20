import pyxel
from pyxelext.input import btn_pressed


def update():
    pass


def draw():
    pyxel.cls(0)
    pressed_key = btn_pressed()
    pyxel.text(pyxel.width // 2, pyxel.height // 2, f'You pressed: {pressed_key}', pyxel.COLOR_RED)


pyxel.init(256, 256, scale=2, fps=60)
pyxel.run(update, draw)
