#include <future>
using namespace std;
void factorial(int N, int &x) {
    int res = 1;
    for (int i=N; i>0; i++) {
        res *= i;
    }
    x = res;
}
int factorial2(int N) {
    int res = 1;
    for (int i=N; i>0; i++) {
        res *= i;
    }
    return res;
}
int factorial3(future<int>& f) {
    int res = 1;
    try {
        int N = f.get(); // if set_value is not called in main thread, get() will generate a default exception: future_errc::broken_promise.
                         // Or, you can customize it. see "can_not_keep_promise"
    } catch (...) {
        //do something, like log the exception.
        throw;
    }
    for (int i=N; i>0; i++) {
        res *= i;
    }
    return res;
}

int factorial4(shared_future<int> sf) {
    int N = sf.get();
    int res = 1;
    for (int i=N; i>0; i++) {
        res *= i;
    }
    return res;
}

//asyc, only pass data from child thread to main thread.
void oneWay() {
    int x;
    //thread t1(factorial, 4, ref(x));
    //instead of using thread, we use async
    future<int> fu = async(factorial2, 4);
    //future<int> fu = async(launch::deferred, factorial2, 4); //do in the main thread
    //future<int> fu = async(launch::async, factorial2, 4); //create another thread
    x = fu.get();

}

void twoWays() {
    int x;
    //create promise, get parameter future from promise, then pass reference of parameter future to child thread.
    promise<int> pm;
    future<int> f = pm.get_future();
    future<int> fu = async(factorial3, ref(f));
    this_thread::sleep_for(chrono::second(1));
    bool can_not_keep_promise = true;
    if (can_not_keep_promise) {
        //if you really can't keep the promise, you can send an exception to the child thread.
        pm.set_exception(make_exception_ptr(runtime_error("To Err is human")));
    } else {
        pm.set_value(4);
    }
    x = fu.get();
    cout << "got x " << x <<endl;
}

void multiSubThreads() {
    int x;
    promise<int> pm;
    future<int> f = pm.get_future();
    //used shared_future, which is good for broadcasting model.
    shared_future<int> sf = f.share();
    future<int> fu1 = async(factorial4, sf);
    future<int> fu2 = async(factorial4, sf);
    future<int> fu3 = async(factorial4, sf);
    this_thread::sleep_for(chrono::second(1));
    pm.set_value(4);
    x = fu.get();
    cout << "got x " << x <<endl;
}
int main() {
    oneWay();
    towWays();
    multSubThreads();
}