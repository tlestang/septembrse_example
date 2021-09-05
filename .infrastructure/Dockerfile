# Base image
FROM quay.io/pypa/manylinux2014_x86_64:2021-08-31-6f90a75

# Install OpenBLAS
RUN yum -y update && yum -y install openblas-devel

# Add source
COPY setup.py pyproject.toml CMakeLists.txt /wheel_build/
ADD pybind11 /wheel_build/pybind11
ADD src /wheel_build/src

WORKDIR /wheel_build

# Wheel build
RUN /opt/python/cp38-cp38/bin/pip wheel .
