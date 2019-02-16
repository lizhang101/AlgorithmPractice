#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <vector>
#include <algorithm>

using namespace std;

class App {
    mutex mtx_;
    condition_variable condvar_;
    bool dataLoaded_;
    public:
    App() {
        dataLoaded_ = false;
    }
    void loadData() {
        cout << "Loading data" << endl;
        this_thread::sleep_for(chrono::milliseconds(100));
        cout << "Data loaded" << endl;
        lock_guard<mutex> guard(mtx_);
        dataLoaded_ = true;
        condvar_.notify_one();
    }

    void mainTask() {
        cout << "main task:" << hex <<this_thread::get_id() << endl;
        unique_lock<mutex> lock(mtx_);
        condvar_.wait(lock, [this] {return dataLoaded_ == true;});
        cout << "got signal" << endl;
    }

};
int main() {
    App app;
    thread thread1(&App::loadData, &app);
    thread thread2(&App::mainTask, &app);
    thread1.join();
    thread2.join();
    vector<int> arr = {1,2,3,4};
    int mul = 0;
    for_each(arr.begin(), arr.end(), [&](int x) { cout << x << endl; mul++; });
    cout << "-----------" <<endl;
    for (auto x : arr) {
        cout << x << endl;
    }
    return 0;
}