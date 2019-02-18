#include <thread> 
using namespace std;

int factorial(int N) {}

int main() {
    /* thread */
    thread(factorial, 6);
    /* mutex */
    mutex mu;
    lock_guard<mutex> locker(mu);
    unique_lock<mutex> ulocker(mu);
    //ulocker.lock();
    //ulocker.unlock();

    //lock(mu1, mu2);
    //unique_lock<mutex>(mu, defer_lock);

    /* condition variable */
    condition_variable cond;
    //cond.wait(ulocker, check());
    //cond.notify_one();

    /* future and promise */
    promise<int> p;
    future<int> f = p.get_future();
    //p.set_value(10);

    /* async() */
    future<int> fu = async(factorial, 6);
    int a = fu.get();

    /* packaged_task */
    packaged_task<int(int)> t (factorial);
    future<int> fu2 = t.get_future();
    t(6);

    /* time constrain */
    this_thread::sleep_for(chrono::millisecond(3));
    chrono::steady_clock::time_point tp = chorno::steady_clock::now() + chrono::microseconds(4);
    this_thread::sleep_until(tp);

    ulocker.try_lock(); //return immediately if can't lock
    ulocker.try_lock_for(chrono::nanoseconds(500));//if can't lock in 500ns, force to return
    ulocker.try_lock_until(tp);

    cond.wait_for(ulocker, chrono::microseconds(2));
    cond.wait_until(ulocker, tp);

    f.get();
    f.wait(); //wait for data to be available
    f.wait_for(chrono::microseconds(2));
    f.wait_until(tp);
}
