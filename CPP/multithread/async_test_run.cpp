#include <chrono>
#include <iostream>
#include <future>
using namespace std;
using namespace std::chrono;

int factorial(future<int> f){
    int N = f.get();
    cout << "N:" << N << endl;
    int res = 1;
    for (int i=N; i>0; i--) {
        res *= i;
    }
    return res;
}
int factorial1(int N) {
    int res = 1;
    for (int i=N; i>0; i--) {
        res *= i;
    }
    return res;
}
class testme {
    void operator()(const string str) {
        cout << str << endl;
    }
};

struct delay {
    void operator() (int(*callback)(int), int N, int M){
        this_thread::sleep_for(chrono::milliseconds(N));
        int res = (*callback)(M);
        cout << "delayed call:" << res << endl;
    }
};



void multiSubThreads() {
    /*
    promise<int> p;
    auto fu = async(launch::async, factorial, move(p.get_future()));
    p.set_value(4);
    cout <<"get factorial:" << fu.get() << endl;
    */
    //auto fu = async(testme, "testme ");
    system_clock::time_point start = system_clock::now();
    auto fu1 = async(launch::async, delay(), factorial1, 300, 1);
    auto fu2 = async(launch::async, delay(), factorial1, 100, 2);
    fu1.get();
    fu2.get();
    auto end = system_clock::now();
 
	auto diff = duration_cast < std::chrono::milliseconds > (end - start).count();
	std::cout << "Total Time Taken = " << diff << " Milliseconds" << std::endl;

}
int main() {
    multiSubThreads();
}