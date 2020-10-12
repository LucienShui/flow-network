from __future__ import absolute_import, print_function
from distutils.core import setup, Extension

module = Extension(name='_core',
                   sources=[
                       'flow-network.cpp',
                       'pyapi.cpp'
                   ],
                   extra_compile_args=[
                       '-std=c++14',
                       '-W',
                       '-fPIC'
                   ])


def build():
    setup(name='core',
          version='0.0.1',
          ext_modules=[module]
          )
