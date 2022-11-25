"""This is a minimal setup.py to be able to use scikit-build

https://scikit-build.readthedocs.io/en/latest/

Project metadata including build-time requirements are declared in the
pyproject.toml file, following PEP621
(https://peps.python.org/pep-0621/).

2022-11-25: Package location location still needs to be passed trough
scikit-build.setup() instead of the pyproject.toml file, as it is
processed by scikit-build.

"""
from skbuild import setup

setup(
    package_dir={'': 'src'},
    packages=["example_pkg"],
    cmake_install_dir="src/example_pkg",
)
