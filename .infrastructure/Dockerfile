# Base image
FROM quay.io/pypa/manylinux2014_x86_64:latest

# Install OpenBLAS
RUN yum -y update && yum -y install openblas-devel

# Add source
COPY setup.py CMakeLists.txt pybind11 src /wheel_build

WORKDIR /wheel_build

# Wheel build
RUN /opt/python/cp38-cp38/bin/pip wheel .
