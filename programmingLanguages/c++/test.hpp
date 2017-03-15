class Test{
public:
    Test():a(0){}
    Test(int a_): a(a_){}
    ~Test(){}
    const int get_a(void) const {return a;}
private:
    const int a;
};
