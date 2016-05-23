
// see https://en.wikipedia.org/wiki/ANSI_escape_code

namespace COLOR{
	const char D_BLACK[]      = "\x1B[30m";
	const char D_BLACK_BG[]   = "\x1B[40m";
	const char D_RED[]        = "\x1B[31m";
	const char D_RED_BG[]     = "\x1B[41m";
	const char D_GREEN[]      = "\x1B[32m";
	const char D_GREEN_BG[]   = "\x1B[42m";
	const char D_YELLOW[]     = "\x1B[33m";
	const char D_YELLOW_BG[]  = "\x1B[43m";
	const char D_BLUE[]       = "\x1B[34m";
	const char D_BLUE_BG[]    = "\x1B[44m";
	const char D_MAGENTA[]    = "\x1B[35m";
	const char D_MAGENTA_BG[] = "\x1B[45m";
	const char D_CYAN[]       = "\x1B[36m";
	const char D_CYAN_BG[]    = "\x1B[46m";
	const char D_WHITE[]      = "\x1B[37m";
	const char D_WHITE_BG[]   = "\x1B[47m";

	const char BLACK[]      = "\x1B[90m";
	const char BLACK_BG[]   = "\x1B[100m";
	const char RED[]        = "\x1B[91m";
	const char RED_BG[]     = "\x1B[101m";
	const char GREEN[]      = "\x1B[92m";
	const char GREEN_BG[]   = "\x1B[102m";
	const char YELLOW[]     = "\x1B[93m";
	const char YELLOW_BG[]  = "\x1B[103m";
	const char BLUE[]       = "\x1B[94m";
	const char BLUE_BG[]    = "\x1B[104m";
	const char MAGENTA[]    = "\x1B[95m";
	const char MAGENTA_BG[] = "\x1B[105m";
	const char CYAN[]       = "\x1B[96m";
	const char CYAN_BG[]    = "\x1B[106m";
	const char WHITE[]      = "\x1B[97m";
	const char WHITE_BG[]   = "\x1B[107m";

	const char BLINK[]      = "\x1B[5m";
	const char RESET[]      = "\x1B[0m";
};

#include<iostream>
using namespace std;
using namespace COLOR;
int main(int argc, char **argv){
	cerr << COLOR::RED << "こんにちは" << COLOR::BLUE << "こんにちは" << COLOR::RESET << endl;
	cerr << "こんばんは。" << endl;
	cerr << COLOR::YELLOW << "黄色です" << endl;
	cerr << COLOR::BLINK << COLOR::WHITE_BG << COLOR::GREEN << "ちかちかしてます。" << COLOR::RESET << endl;

	
	for(int i = 0; i != 108; ++i){
		cerr << "\x1B[" << i << "m:::" << i << ": こんにちは" << COLOR::RESET << endl; 
	}

}


