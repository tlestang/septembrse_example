"""Setup example package
"""
from setuptools import find_packages
from skbuild import setup

setup(
    name='septembrse',
    license='GPLv3',
    description='A simple example package for the walkthrough',
    author='Thibault Lestang',
    author_email='thibault.lestang@protonmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    cmake_install_dir="src/example_pkg",
)
