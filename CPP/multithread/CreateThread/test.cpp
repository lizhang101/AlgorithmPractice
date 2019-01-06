#include <thread>
#include <iostream>
using namespace std;
class ThreadRAII {
    thread &thread_;
    public:
    ThreadRAII(thread &thd) : thread_(thd) {

    }
    ~ThreadRAII() {
        if (thread_.joinable()) {
            thread_.detach();
        }
    }
};

void thread_func() {
    for (int i = 0; i < 100; i++) {
        std::cout <<"thread function executing" <<std::endl;
    }
}

int main() {
    thread threadObj(thread_func);
    cout << "thread created" << endl;
    ThreadRAII wrapperObj(threadObj);
    cout<< "main exit" << endl;
    return 0;
}