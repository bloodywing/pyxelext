import pyxel
import re
from textwrap import wrap

px_c = 4


def text(x: int, y: int, txt: str):
    """

    Multicolor text, where you format your text within the text

    :param x: x position on screen
    :param y: y position on screen
    :param txt: String that should be rendered, use \p[0-15] to set a color from the palette
    :return:
    :example:

    text(0, 0, "\p1Hello \p16Pyxel")
    """
    _l = 0
    _p = re.compile(r'^(\d{,2})(.*)')
    for t in txt.split(r'\p'):
        if t:
            _c, _text = _p.match(t).group(1, 2)
            if not _c:
                _c = 0
            pyxel.text(x + _l, y, _text, int(_c))
            _l = len(_text) * px_c


def textblock(x: int, y: int, txt: str, nl_px: int = 6, drop_whitespace: bool = True):
    """
    Text automatically wraps at screen edge, if the text looks strange set drop_whitespace to False
    also uses text() to actually render the text. When a linewrapp occurs the new line is at x + nl_px
    :param x: x position on screen
    :param y: y position on screen
    :param nl_px: addjust this for linespace, a value of 6 leaves a small space between lines
    :param txt: Your text that should be rendered. You can use \p and manual linebreaks with \n
    """
    if x + len(txt.replace(r'\p', '')) * px_c > pyxel.width:
        # oops text is outside of screen, wrap it
        chars_available = (pyxel.width - x) // px_c - 2
        for t in txt.splitlines():
            new_txts = wrap(t, int(chars_available),
                            drop_whitespace=drop_whitespace)
            for new_txt in new_txts:
                text(x, y, new_txt)
                y += nl_px
