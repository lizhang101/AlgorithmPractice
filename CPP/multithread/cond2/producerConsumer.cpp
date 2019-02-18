#include <queue>
#include <mutex>
#include <condition_variable>
mutex mu;
queue<int> q;
//Bad busy wait example >>>>>

void producer() {
    int count = 10;
    while (count) {
        {
            lock_guard<mutex> lk(mu);
            q.push(count);
        }
        this_thread::sleep_for(chrono::second(1));
        count--;
    }
}

void consumer() {
    int data = 0;
    while (true){
        unique_lock<mutex> lk(mu);
        if (q.empty()) {
            lk.unlock();
        } else {
            data = q.front();
            q.pop();
            lk.unlock();
            //printing stands for data processing
            cout << data << endl;
        }
    }
}


//<<<<<
//Condition variable version >>>>
condition_variable cond;

void producer() {
    int count = 10;
    while (count) {
        unique_lock<mutex> lk(mu);
        q.push(count);
        lk.unlock();
        cond.notify_one;
        this_thread::sleep_for(chrono::second(1));
        count--;
    }
}

void consumer() {
    int data = 0;
    while (true){
        unique_lock<mutex> lk(mu);
        //comsumer can be wake up by itself. so we have to check the condition even if there is one thread to wake the consumer thread.
        cond.wait(lk, []() { return !q.empty(); });
        data = q.front();
        q.pop();
        lk.unlock();
        //printing stands for data processing
        cout << data << endl;
    }
}



//<<<<<