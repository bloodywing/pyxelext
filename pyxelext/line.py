import pyxel
import math


def line(x1: int, y1: int, x2: int, y2: int, col: int) -> int:
    """
    This function is exactly like pyxel's line function but returns the length of the drawn line

    :return: length of the line
    """
    pyxel.line(x1, y1, x2, y2, col)
    return int(math.hypot(x1 - x2, y1 - y2))


def aline(x: int, y: int, length: int, col: int, angle: int = 0) -> [int, int]:
    """
    Draws a angled line. Because lazy math

    :param x: start X position
    :param y: start Y position
    :param length: length of the line in pixels
    :param col: colour as integer, see pyxel for that
    :param angle: angle of the line in degree. Use 0 for a horizontal line towards right
    :return:
    :see
    :example:

    aline(50, 50, 20, pyxel.COLOR_WHITE, 90)
    """
    x2, y2 = int(x + length * math.cos(angle * math.pi / 180)), int(y + length * math.sin(angle * math.pi / 180))
    pyxel.line(x, y, x2, y2, col)
    return x2, y2


def poly(*args: ((int, int),), col: int):
    """
    Draws a polygon with the help of lines and vertices

    :param args: Multiple vericles in (x, y)
    :param col: Pyxel palette color in integer
    :return:
    """

    assert len(args) > 1
    for r in range(len(args)):
        vert_1 = args[r]
        vert_2 = args[0] if r == len(args) - 1 else args[r+1]
        pyxel.line(*vert_1, *vert_2, col)
