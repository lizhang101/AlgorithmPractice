#include <thread>
using namespace std;
class A {
    void f(int x, char c) {}
    long g(double x) { return 0; }
    int operator()(int N) { return 0; }
};

void foo(int x) {

}

int main() {
    A a;
    thread t1(a, 4); // create a copy of a in a different thread;
    thread t2(ref(a), 4); // passing by reference to a different thread.
    thread t2(move(a), 4); // move
    thread t3(A(), 4); // temp A
    thread t3([](int x){return x*x; }, 4); // lambda 
    thread t4(foo, 7);
    thread t5(&A::f, a, 8, 'W'); //copy_of_a.f(8, 'w') in a different thread
    thread t5(&A::f, &a, 8, 'W'); // a.f(8, w) in a different thread
    
    async(a, 4);
    bind(a, 6);
    call_once(once_flag, a, 6);
}