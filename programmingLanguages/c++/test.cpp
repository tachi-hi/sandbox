#include<iostream>
#include<memory>
#include"test.hpp"

int main(int argc, char** argv){
    auto t = Test(3);
    int c = t.get_a();
    c += 1;
    std::cerr << c << std::endl;


    //std::shared_ptr<Test> t2 = std::make_shared<Test>(3);
    auto t2 = std::make_shared<Test>(3);
    c = t2->get_a(); // autocomplete-clang can also find the member function if it is insider of the shared_ptr.
    std::cerr << c << std::endl;

}
