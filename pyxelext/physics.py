import pyxel
from .line import poly
try:
    import pymunk
except ImportError:
    print('You need pymunk in order to use pyxelext.physics. Stopping application.')
    exit(1)

# todo physics support for sprites, images, tilesets


def debug_draw_options():
    """
    Debug draw function. Keep in mind that this has a huge impact on performance. Use it only for debugging and testing
    :example:

    space = pymunk.Space()

    def draw():
        pyxel.cls(0)
        debug_draw(space)

    :param space:
    :return:
    """

    def debug_draw_circle(pos, angle, radius, outline_color, fill_color, data=None):
        pyxel.circ(*pos, r=radius-1, col=fill_color)
        pyxel.circb(*pos, r=radius, col=outline_color)

    def debug_draw_dot(size, pos, color):
        pyxel.pset(*pos, color)

    def debug_draw_segment(a, b, color):
        pyxel.line(*a, *b, col=color)

    def debug_draw_polygon(vs, radius, outline_color, fill_color):
        poly(*vs, col=outline_color)

    def _c(color):
        return sum([color.r, color.g, color.b]) % 15

    options = pymunk.SpaceDebugDrawOptions()
    options.draw_circle = debug_draw_circle
    options.draw_dot = debug_draw_dot
    options.draw_segment = debug_draw_segment
    options._c = _c
    options.draw_polygon = debug_draw_polygon
    return options


def static_rect(x: int, y: int, w: int, h: int, col: int, space: pymunk.Space, **kwargs):
    """
    Draws a static rectb with collisions.
    :return:
    :param kwargs: addition keyword args for Poly. Check pymonk.Poly docs for that. Exmaple: friction
    """
    pyxel.rect(x, y, w, h, col)
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x + w // 2, y + h // 2)  # pymunk uses gravity center
    # No extra body because it's  static without any properties
    s = pymunk.Poly.create_box(body, size=(w, h))
    for k, v in kwargs.items():
        setattr(s, k, v)
    space.add(s)


def static_circ(x: int, y: int, r: int, col: int, space: pymunk.Space, **kwargs):
    pyxel.circ(x, y, r, col)
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x, y)
    s = pymunk.Circle(body, radius=r)
    for k, v in kwargs.items():
        setattr(s, k, v)
    space.add(s)


def oopv_sleep(space: pymunk.Space, r=0):
    """
    Out of pyxel's  bounds objects are forced sleeping.

    :param space:
    :param r: adds additional radius around the size of pyxel. so objects won't go to sleep
              if they just left the visible view
    :return:
    """
    for o in space.bodies:  # type: pymunk.Body
        if not o.is_sleeping:
            if o.position.x > pyxel.width + r and o.position.y > pyxel.height + r:
                o.sleep()
                continue
            if o.position.x < 0 - r and o.position.y < 0 - r:
                o.sleep()
                continue
