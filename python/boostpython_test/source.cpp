#include"Python.h"
#include<boost/python.hpp>
#include<boost/python/numeric.hpp>

int myFunc(int lhs, int rhs){
	return lhs + rhs;
}

BOOST_PYTHON_MODULE( myPackageName ){

	boost::python::def("myFunctionBoost", &myFunc);

}


