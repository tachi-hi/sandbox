

PythonLIBS = `pkg-config --cflags --libs python2`

all:
	g++ -Wall -O2 ${PythonLIBS} -DPIC -shared -fPIC -o myPackageName.so source.cpp -lboost_python
	

