from __future__ import absolute_import, print_function
import ctypes
from os import path


class Clib:

    def __init__(self, raw_lib_path: str = '_core.so'):
        this_directory = path.abspath(path.dirname(__file__))
        lib_path = path.join(this_directory, raw_lib_path)

        if not path.exists(lib_path):
            raise AssertionError(f'{lib_path} not found')

        self._clib = ctypes.cdll.LoadLibrary(lib_path)
