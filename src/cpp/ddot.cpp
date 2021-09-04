#include <cblas.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double ddot(py::array_t<double> Xpy, py::array_t<double> Ypy) {

  auto x = Xpy.unchecked<1>();
  auto y = Ypy.unchecked<1>();
  // Create arrays that represent the matrices X, Y
  const int n = x.size();
  double*  X = new double[n];
  double*  Y = new double[n];

  // Fill X and Y
  for(uint i =0; i <n; i++){
    X[i] = x[i];
    Y[i] = y[i];
  }

  // Calculate X dot Y
  double res = cblas_ddot(n, X, 1, Y, 1);

  // Clean up
  delete[] X;
  delete[] Y;

  return res;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("ddot", &ddot, "A function which computes the dot product of two vectors.");
}
