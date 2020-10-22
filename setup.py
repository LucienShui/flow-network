from __future__ import absolute_import, print_function

import os

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from shutil import move

from flow_network.__version__ import __title__, __description__, __url__
from flow_network.__version__ import __version__, __author__
from flow_network.__version__ import __author_email__


def readme(filename: str = 'README.md') -> str:
    """
    read the contents of your README.md file
    :return: contents of README.md
    """

    this_directory = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(this_directory, filename), encoding='utf-8') as file:
        return file.read()


class CustomExtension(Extension):
    def __init__(self, name, sources, base_dir, *args, **kw):
        super().__init__(name, sources, *args, **kw)
        self.base_dir = base_dir


class CustomBuild(build_ext):
    def build_extension(self, ext: CustomExtension):
        if isinstance(ext, CustomExtension):
            ext.sources = [os.path.join(ext.base_dir, each) for each in ext.sources]

        super().build_extension(ext)

        if isinstance(ext, CustomExtension):
            raw_output = self.get_ext_fullpath(ext.name)

            filename = os.path.basename(raw_output)
            pathname = os.path.dirname(raw_output)

            output = os.path.join(pathname, ext.base_dir, filename)

            move(raw_output, output)


if __name__ == '__main__':
    custom_extension = CustomExtension(name='_core',
                                       sources=['graph.cpp', 'base_network.cpp', 'maximum_flow.cpp',
                                                'minimum_cost_flow.cpp', 'core_wrap.cxx'],
                                       base_dir='flow_network/core',
                                       extra_compile_args=['-std=c++11'])

    setup(
        name=__title__,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        url=__url__,
        description=__description__,
        packages=find_packages(),
        ext_modules=[custom_extension],
        cmdclass={'build_ext': CustomBuild},
        long_description=readme(),
        long_description_content_type='text/markdown'
    )
