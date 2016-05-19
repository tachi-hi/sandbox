#include "lua.hpp"
#include "lauxlib.h"
#include "lualib.h"

#include<iostream>
using namespace std;

// macro with typeinfo
#include<typeinfo>
#include<cxxabi.h>
char* demangle(const char *demangle) {
    if (false){
        return const_cast<char*>(demangle); // unless required to demangle the type, use this
    }else{
        int status;
        return abi::__cxa_demangle(demangle, 0, 0, &status);
    }
}
#define SHOW_v(x) cerr << #x << " (type: " << demangle(typeid(x).name()) << " )== " << x << endl

// main
int main(int argc, char**argv){
    lua_State *L = luaL_newstate(); // define Lua state
    luaL_openlibs(L); // load sandard libraries

    // exec Lua script written in a file
    luaL_loadfile(L, "test.lua");
    lua_pcall(L, 0, 0, 0);

    // get variable in L
    lua_getglobal(L, "a");
    lua_getglobal(L, "b");
    lua_getglobal(L, "c");
    lua_getglobal(L, "s");
    int a  = lua_tonumber(L, 1); // bottom (oldest) of the stack
    int b  = lua_tointeger(L, 2); // 2nd
    int c  = lua_tonumber(L, 3); // 3rd
    double c_2  = lua_tonumber(L, -2); // 2nd latest
    const char* s = lua_tostring(L,4); // 4th
    std::string ss (lua_tostring(L,-1)); // top (latest) of the stack
    // maximum size of stack is 20.
    // If more variables are needed other functions are required.
    SHOW_v(a);
    SHOW_v(b);
    SHOW_v(c);
    SHOW_v(c_2);
    SHOW_v(s);
    SHOW_v(ss);

    // exec a function in lua script
    double x = 3; double yyy = 4;
    lua_getglobal(L, "radius");
    lua_pushnumber(L, x);
    lua_pushnumber(L, yyy);
    lua_pcall(L, 2/*num of args*/, 1/*num of ret value*/, 0/*error function*/);
    double radius = lua_tonumber(L, -1); // get latest value on the stack
    SHOW_v(radius);
    double radius2 = lua_tonumber(L, -1); // get latest value on the stack
    SHOW_v(radius2);

    lua_getglobal(L, "decimal");
    lua_pushinteger(L, x); // 1st arg
    lua_pushnumber(L, yyy); // 2nd arg
    lua_pushinteger(L, 9.0); // 3rd arg (directly pass a constant)
    lua_pushstring(L, " YEN"); // 2nd arg
    lua_pcall(L, 4, 1, 0);
    const char* decimal = lua_tostring(L, -1); // get latest value on the stack
    SHOW_v(decimal);

    return 0;

}
