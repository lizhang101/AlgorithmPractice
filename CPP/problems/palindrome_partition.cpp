#include <iostream>
bool isParlindrome(const string &str, int left, int right) {
    int l = left;
    int r = right;
    while (l < r){
        if (str[l] != str[r]) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}
int minCuts(const string &str){
    vector<int> dp(str.size(), str.size());
    dp[0] = 0;
    for (int i = 1; i<str.size(); ++i) {
        if (isParlindrome(str, 0, i)) {
            dp[i] = 0;
        } else {
            for (int j = 1; j <= i; ++j) {
                if (isParlindrome(str, j, i)) {
                    dp[i] = min(dp[i], dp[j-1]+1);
                }
            }
        }
    }
    return dp[str.size()-1];
}
int main() {
    printf("string: %s cuts:%d\n", "abab", minCuts(string("abab")));
}