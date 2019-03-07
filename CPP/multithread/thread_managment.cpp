/* functor, thread RAII wrapper, */

#include <iostream>
#include <thread>
#include <string>
#include <memory>
using namespace std;

void function_1() {
    cout << "function_1\n";
}

struct Fctor {
    void operator() (string &msg) {
        cout << "says:" << msg << endl;
    }

    void operator() (string &&msg) {
        cout << "says:" << msg << endl;
    }

    //Note: dont get the raw pointer of msg or using refernece to it.
    void operator() (unique_ptr<string> msg) {
        cout << "says:" << *msg << endl;
    }




    void operator() () {
        cout << "says:" << "nothing." << endl;
    }
};


void use_factor_1() {
    Fctor fct;
    thread t1(fct);
    cout << "t1 tid:" << t1.get_id() << endl;
    t1.join();
}
void use_factor_2() {
    //1. create Functor directly.
    //2. pass parameter by reference so it can be changed in child thread.
    //3. passing by reference may have data race conditions. Better to use move
    string s = "passing by reference";
    thread t1((Fctor()), std::ref(s));
    t1.join();
}

void use_factor_3() {
    //3. passing by reference may have data race conditions. Better to use move
    //   This will call operator that takes rvalue reference.
    //   Best is to use a unique_ptr for move
    string s = "passing by using move";
    thread t1((Fctor()), std::move(s));
    t1.join();
    auto p_s = make_unique<string>("passing by using move + unique_ptr");
    thread t2((Fctor()), std::move(p_s));
    t2.join();

}
void move_thread() {
    auto p_s = make_unique<string>("moving thread");
    thread t1((Fctor()), std::move(p_s));
    thread t2(move(t1));
    //Note we don't call t1.join() anymore.
    t2.join();
}

int main() {
    cout << "thread id:" << this_thread::get_id() << " main\n";
    use_factor_1();
    use_factor_2();
    use_factor_3();
    move_thread();



    return 0;
}