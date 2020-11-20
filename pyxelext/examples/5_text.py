import pyxel
from pyxelext.text import text, textblock


def update():
    pass


def draw():
    pyxel.cls(15)
    text(100, 128, f'\p2Many colors! \p{pyxel.frame_count % 16}uwu')
    text(100, 138, f'\p4HELLO!')
    text(100, 148, f'No Palette Escape uses color 0')

    textblock(100, 0, 'This is\na very very very very very very very '
                      'very very very very \p8very very very very long text block')


pyxel.init(256, 256, scale=2)
pyxel.run(update, draw)
