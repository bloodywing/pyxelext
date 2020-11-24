import pyxel
import pymunk
from pyxelext.physics import static_rect, static_circ, debug_draw_options, oopv_sleep

space = pymunk.Space()
space.sleep_time_threshold = .01
space.gravity = (0, 900)


def update():
    pass


class Particle:

    body = None
    poly = None
    color = pyxel.COLOR_YELLOW

    def __init__(self, startpos=()):
        self.body = pymunk.Body(0.01, 10)
        self.body.position = startpos
        self.poly = pymunk.Circle(self.body, 1)
        self.poly.friction = 0.3
        space.add(self.body, self.poly)


particles = []

options = debug_draw_options()


def draw():
    for step in range(5):
        space.step(0.007/5)
    pyxel.cls(0)
    space.debug_draw(options)
    oopv_sleep(space, 1)

    for i, p in enumerate(particles):
        pyxel.text(0, 0+7*i, str(p.body.is_sleeping), col=pyxel.COLOR_RED)

    static_circ(100, 70, 5, pyxel.COLOR_LIGHTBLUE, space, friction=1)
    static_rect(50, 120, 120, 10, pyxel.COLOR_RED, space, friction=1)


for r1 in range(5):
    for r2 in range(2):
        particles.append(Particle(startpos=(80+r1, r2)))

pyxel.init(256, 256, scale=2, fps=60)
pyxel.run(update, draw)
