import pyxel
from os import PathLike
import sdl2
try:
    from PIL import Image
    has_pil = True
except ImportError:
    has_pil = False

pyxel.is_fullscreen = False


def set_fullscreen(real_fullscreen: bool = False):
    """
    Activates Fullscreen, for the Pyxel window

    :return:
    :rtype:
    """
    current_window = sdl2.SDL_GL_GetCurrentWindow()
    sdl2.SDL_SetWindowFullscreen(current_window, sdl2.SDL_WINDOW_FULLSCREEN if real_fullscreen else sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
    pyxel.is_fullscreen = True


def set_windowed():
    """

    Activates windowed mode for Pyxel

    :return:
    :rtype:
    """
    current_window = sdl2.SDL_GL_GetCurrentWindow()
    sdl2.SDL_SetWindowFullscreen(current_window, 0)
    pyxel.is_fullscreen = False


def set_window_icon(icon: PathLike, bytes_per_pixel: int = 4):
    """
    Lets you set a custom window icon for pyxel. you can call this after pyxel.init
    """

    if not has_pil:
        RuntimeWarning('You need Pillow/PIL in order to use pyxelext.system.set_window_icon')
        return

    current_window = sdl2.SDL_GL_GetCurrentWindow()
    img = Image.open(icon)
    x, y = img.size
    rmask = 0x000000ff
    gmask = 0x0000ff00
    bmask = 0x00ff0000
    amask = 0 if bytes_per_pixel == 3 else 0xff000000
    icon_surface = sdl2.SDL_CreateRGBSurfaceFrom(img.tobytes(), x, y, bytes_per_pixel*8, bytes_per_pixel*x, rmask, gmask, bmask, amask)

    sdl2.SDL_SetWindowIcon(current_window, icon_surface)
    sdl2.SDL_FreeSurface(icon_surface)
