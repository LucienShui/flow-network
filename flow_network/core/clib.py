from __future__ import absolute_import, print_function
import ctypes
from distutils.sysconfig import get_config_var
from os import path


class Clib:

    def __init__(self, raw_lib_path: str = '_core'):
        this_directory = path.abspath(path.dirname(__file__))
        lib_path = path.join(this_directory, f'{raw_lib_path}{get_config_var("EXT_SUFFIX")}')

        if not path.exists(lib_path):
            raise AssertionError(f'{lib_path} not found')

        self._clib = ctypes.cdll.LoadLibrary(lib_path)
