#include <iostream>
using namcspace std;

int factorial (int N) {
    int res = 1;
    for (int i=N; i>1; i--)  {
        res *= i;
    }

    cout << "res is : " << res << endl;
    return res;
}

deque<packaged_task<int()>> task_q;
mutex mu;
condition_variable cond;

void thread_1() {
    packaged_task<int()> t;
    {
        unique_lock<mutex> locker(mu);
        cond.wait(locker, []() {return !task_q.empty(); });
        t = move(task_q.front());
        task_q.pop_front();
    }
    t();
}

int main() {
    //the template type is the same as function signature.
    packaged_task<int(int)> t(factorial);
    packaged_task<int()> t1(bind(factorial, 6));//create a function object with a parameter
    auto fo1 = std::bind(factorial, 6);
    ////


    t(6); //in a different thread
    t(); //in a different thread
    //In following example, we create a packaged_task, push into a queue, and service_th will pop it and execute it in another thread.
    thread service_th(thread_1);
    packaged_task<int()> tt(bind(factorial, 6));
    future<int> fu = tt.get_future();
    {
        lock_guard<mutex> locker(mu);
        task_q.push_back(move(tt));
    }
    cond.notify_one();

    cout << fu.get();
    service_th.join();

    return 0;
}
/*
3 ways to get a future:
* - promise::get_future()
* - packaged_task::get_future()
* - async() returns a future
*/