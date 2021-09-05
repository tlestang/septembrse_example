cmake_minimum_required(VERSION 3.10)
project(snail)

set(CPP_SRC_DIR src/cpp)

add_subdirectory(pybind11)
pybind11_add_module(ddot
  ${CPP_SRC_DIR}/ddot.cpp
  )
# To find Homebrew's openblas on macos
set(DCMAKE_PREFIX_PATH "/usr/local/opt/lapack;/usr/local/opt/openblas")
find_package(BLAS)
find_path(BLAS_INCLUDE_DIRS cblas.h
  /usr/include
  /usr/local/include
  /usr/include/openblas
  $ENV{BLAS_HOME}/include)
target_include_directories(ddot PRIVATE ${BLAS_INCLUDE_DIRS})
target_link_libraries(ddot PRIVATE ${BLAS_LIBRARIES})
install(TARGETS ddot LIBRARY DESTINATION .)
