cmake_minimum_required(VERSION 3.10)
project(snail)

set(CPP_SRC_DIR src/cpp)

add_subdirectory(pybind11)
pybind11_add_module(extension
  ${CPP_SRC_DIR}/ext.cpp
)
install(TARGETS extension LIBRARY DESTINATION .)
