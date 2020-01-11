#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    auto cmp = [](const vector<int> &a, const vector<int> &b){ return a[0]>b[0]; };
    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp) > pq;
    pq.push({3,1});
    pq.push({4, -2});
    pq.push({4, -1});
    pq.push({4, -3});
    pq.push({2, -2});
    while (pq.size()) {
        auto pt = pq.top();
        pq.pop();
        cout << pt[0] << " " << pt[1] << endl;
    }

}