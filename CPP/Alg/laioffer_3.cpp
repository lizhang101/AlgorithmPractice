//#1
vector<string> insertSpace(const string& str){
    vector<string> res;
    string cur = str;
    helper(res, cur, 0, str.size());
    return res;
}

void helper(vector<string> &res, string& cur, int s, int e){
    res.push_back(cur);
    for (int i = s; i<e-1; ++i) {
        //string cur2 = substr(cur, s, i-s+1) + "_" + substr(cur, i+1, e-i);
        cur.insert(i, "_");
        helper(res, cur, s, i);
        helper(res, cur, i+2, e+1);
    }
}

//#2
bool isCousin(TreeNode*root, int a, int b) {
    if (root == nullptr) { return false; }
    if (root->left == nullptr || root->right == nullptr) { return false; }
    queue<TreeNode*> que, cur;
    que.push(root);
    while (!que.empty()){
        cur = que;
        bool found_a = false, found_b = false;
        while (!cur.empty()) {
            auto r = cur.front();
            cur.pop();
            bool cur_found_a = (r->left && (r->left->val == a) || r->right && (r->right->val == a));
            bool cur_found_b = (r->left && (r->left->val == b) || r->right && (r->right->val == b));
            if (cur_found_a && cur_found_b) { return false; }
            found_a = found_a || cur_found_a;
            found_b = found_b || cur_found_b;
            if (found_a && found_b) {return true;}
            if (r->left) { que.push(r->left); }
            if (r->right) { que.push(r->right); }
        }
    }
    return false;
}

//#3
int splitSquare(int N){
    if (N==0) {return 0;}
    vector<int> dp(N+1, INT_MAX);
    dp[0] = 0;
    dp[1] = 1;
    for (int i=1, i<=N; ++i) {
        for (int j=1; j*j<=i; ++j) {
            if (j*j == i) { 
                dp[i] = 1; 
                break;
            }
            dp[i] = min(dp[i], dp[j] + dp[N-j]);
        }
    }
    return dp[N];
}

//#4
unordered_map<char, unordered_set<char>> graph;
unordered_map<char, unordered_map<char, int>> counts;
visited;
bool canCircle(const vector<string>& strings) {
    for (auto &str : strings) {
        if (str == "") { return false; }
        char a = str[0];
        char b = str[str.size()-1];
        counts[a][b]++;
        graph[a].insert(b);
    }
    bool dfs(char start, int &cnt){
        for (auto c : graph[start]) {
            if (counts[start][c] == 0) { 
                return cnt == total_strings_;
            }
            counts[start][c] --;
            cnt ++;
            if (dfs(c, cnt)) { return true; }
            cnt --;
        }
        return false;
    }
}