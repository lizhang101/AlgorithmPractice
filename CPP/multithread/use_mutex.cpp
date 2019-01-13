#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
using namespace std;

class Wallet {
  int money_;
  mutex mtx_;
  public:
  Wallet() : money_(0) {}
  int getMoney() { return money_; }
  void addMoney(int m) { 
    // Note
    lock_guard<mutex> lock(mtx_);
    for (int i=0; i < m; ++i) {
      money_++;
    }
  }
};

int testAddMoney() {
  Wallet wallet;
  vector<thread> threads;
  for (int i=0; i<5; ++i) {
    threads.push_back(thread(&Wallet::addMoney, &wallet, 1000));
  }
  for(auto &th : threads) {
    th.join();
  }
  return wallet.getMoney();
}

// To execute C++, please define "int main()"
int main() {
  for (int k=0; k<10; ++k) {
    int val = 0;
    if ((val = testAddMoney()) != 5000)  cout << val << endl;
    else cout << "got lucky" << endl;
  }
  cout <<"End" <<endl;
}