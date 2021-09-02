cmake_minimum_required(VERSION 3.10)
project(snail)

set(CPP_SRC_DIR src/cpp)

add_subdirectory(pybind11)
pybind11_add_module(example
  ${CPP_SRC_DIR}/ddot.cpp
  )
find_package(BLAS)
target_link_libraries(example PRIVATE ${BLAS_LIBRARIES})
install(TARGETS example LIBRARY DESTINATION .)
