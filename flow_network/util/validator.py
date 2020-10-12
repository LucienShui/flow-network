from __future__ import absolute_import, print_function


def index_validator(u: int, v: int, n: int) -> bool:
    if u < 0:
        raise AssertionError(f'index of u is {u}, which should be greater or equal to 0')

    if u >= n:
        raise AssertionError(f'index of u is {u}, which should be less than n = {n}')

    if v < 0:
        raise AssertionError(f'index of v is {v}, which should be greater or equal to 0')

    if v >= n:
        raise AssertionError(f'index of v is {v}, which should be less than n = {n}')

    return True
