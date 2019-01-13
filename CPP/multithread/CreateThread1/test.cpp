#include <iostream>
#include <thread>
using namespace std;

// To execute C++, please define "int main()"
void testme () {
  for (int i=0; i<10; ++i) {
    cout<<"testme:" << i << endl;
  }
}

class TestThread {
  public:
  void operator() (){
    for (int i = 0; i < 10; i++) { 
      cout << "thread:" << hex << this_thread::get_id() << " " << i << endl; 
    } 
  }
};
class ThreadWrapper {
  thread &thread_;
  public:
  ThreadWrapper(thread &th) : thread_(th) { }
  ~ThreadWrapper() {
    //always check if the thread is joinable before calling join or detach.
    if (thread_.joinable()) {
      thread_.join();
    }
  }
};

class Wallet {
  int money_;
  public:
  Wallet() : money_(0) {}
  int getMoney() { return money_; }
  void addMoney(int m) { 
    for (int i = 0; i < m; ++ i) {
      money_++;
    }
  }
};



int main() {
  //3 methods to create a thread 
  //thread threadobj(testme);
  //thread threadobj( (TestThread()) );
  thread threadobj([]() {for (int i = 0; i < 10; i++) { cout << "thread:" << hex << this_thread::get_id() << " " << i << endl; }} );
  ThreadWrapper wrapper(threadobj);
  cout << "main: started thread" << endl;
  for (int i = 0; i<10; i++) {
    cout << "main:" << hex << this_thread::get_id() <<" " << i << endl;
  }
  return 0;
}
