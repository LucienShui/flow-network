from __future__ import absolute_import, print_function

from setuptools import setup, find_packages
from os import path, system


def readme(filename: str = 'README.md') -> str:
    """
    read the contents of your README.md file
    :return: contents of README.md
    """

    this_directory = path.abspath(path.dirname(__file__))

    with open(path.join(this_directory, filename), encoding='utf-8') as file:
        return file.read()


commands = [
    'cd flow_network/core && make'
]


for command in commands:
    system(command)


setup(
    name='flow-network',
    version='0.0.1',
    author='Lucien Shui',
    author_email='lucien@lucien.ink',
    url='https://github.com/LucienShui/flow-network',
    description='Flow Network C++ Implementation',
    packages=find_packages(),
    long_description=readme(),
    include_package_data=True,
    long_description_content_type='text/markdown'
)
