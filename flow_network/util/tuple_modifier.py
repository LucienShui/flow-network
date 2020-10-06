from __future__ import absolute_import, print_function


def tuple_modifier(obj: tuple, idx: int, value) -> tuple:
    buf = list(obj)
    buf[idx] = value
    return tuple(buf)
