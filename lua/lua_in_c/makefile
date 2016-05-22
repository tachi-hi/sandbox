LUA:=$(shell pkg-config --list-all | grep lua | cut -d" " -f1)

INCLUDE:=$(shell pkg-config --cflags $(LUA))
LDFLAGS:=$(shell pkg-config --libs $(LUA))
all:
	echo $(LUA)
	g++ -o test $(INCLUDE) test.cpp $(LDFLAGS)

