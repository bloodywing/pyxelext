import pyxel


def btn_pressed():
    """
    Returns the key that was pressed at the current frame. Place this in a draw or update callback

    :see: https://github.com/kitao/pyxel/issues/271
    :return:
    """
    for k in pyxel.__dict__.keys():
        if (
            k.startswith('KEY_')
            or k.startswith('GAMEPAD_')
            or k.startswith('MOUSE_')
        ) and pyxel.btn(getattr(pyxel, k)):
            return k
