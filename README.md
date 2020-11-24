**PyxelExt** are lazy Pyxel extensions.

This is my personal collection of functions that I need, or _might need_ for my game(s).

## Install

    pip install pyxelext
    
## Functions

### Take a look in `pyxelext/examples`

`# pyxelext/line.py`
```python
from pyxelext.line import *
line(x1: int, y1: int, x2: int, y2: int, col: int)  # like pyxel.line but returns length of the line in pixel
aline(x: int, y: int, length: int, col: int, angle: int = 0)
poly(*args: ((int, int),), col: int)  # draw a polygon
```

![draw aline in action](pyxelext/examples/images/draw_aline.gif "draw aline in action")

`# pyxelext/input.py`
```python
from pyxelext.input import *
btn_pressed()  # returns button that is currently pressed
```

`# pyxelext/text.py`
```python
from pyxelext.text import *
text(x: int, y: int, txt: str)  # pyxel.text but with inline text palette support
textblock(x: int, y: int, txt: str, nl_px: int = 6, drop_whitespace: bool = True)  # Text block with screen wrap
```

![text in action](pyxelext/examples/images/text.gif "text in action")

`# pyxelext/physics.py`
Needs `pymunk` in order to work.
```python
debug_draw_options() #  pretty much similar to pygame function in pymunk.
static_rect(x: int, y: int, w: int, h: int, col: int, space: pymunk.Space, **kwargs)  # static rectangle from pyxel
static_circ(x: int, y: int, r: int, col: int, space: pymunk.Space, **kwargs)  # static circle
oopv_sleep(space: pymunk.Space, r=0)  # put this in your draw function so bodies in space will be inactive once they've left the pyxel screen
```

`# pyxelext/system.py`
Adds features to pyxel that are currently not implemented in the main library
```python
set_fullscreen(real_fullscreen: bool = False)  # enables fullscreen, real_fullscreen changes desktop resolution as well
set_windowed()  # enables windowed mode
set_window_icon(icon: PathLike, bytes_per_pixel: int = 4)  # lets you set your own icon for the window title. tested with png and .ico with alpha
```
