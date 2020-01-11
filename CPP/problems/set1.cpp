void place(vector<vector<int>> &board, int r, int n, set<int> &cols, set<int> &diag1, set<int> &diag2) {
    if (r == n) {
        PrintAarry(board);
        return;
    }
    for (int i = 0; i < n; i++)
    {
        if (cols.count(i) != 0 || diag1.count(r + i) != 0 || diag2.count(r - i) != 0)
        {
            continue;
        }
        board[r][i] = 1;
        cols.insert(i);
        diag1.insert(r + i);
        diag2.insert(r - i);
        place(board, r + 1, n, cols, diag1, diag2);
        board[r][i] = 0;
        cols.erase(i);
        diags.erase(r + i);
        diag2.erease(r - i);
    }
}
void nQueens(int n) {
    set<int> cols, diag1, diag2;
    vector<vector<int>> board;
    place(board, cols, 0, diag1, diag2);
}

//-----------------------------
class Solution{
    int max_;
    public:
    int maxPathSum(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }

        int left = maxPathSum(root->left);
        int right = maxPathSum(root->right);
        int submax = max(left, right)+root->val;
        max_ = max(max_, submax, left+right+root->val);
        return submax;
    }
};

//---------------------------3
class Solution{
    int cuts_;
    int max_cuts_;
    unordered_map<pair<int, int>, bool>> memo;
    public:
    int getMinCuts(const string &str) {
        max_cuts_ = 0;
        minCuts(str, 0, str.size()-1, 0);
        return max_cuts_;
    }
    int minCuts(const string& str, int start, int end, int cuts)
    {
        if (start == end) {
            max_cuts_ = max(max_cuts_, cuts);
            return true;
        }
        for (int i = end, i >= start; --i){
            if (isParlidrome(str, start, i)){
                if (minCuts(str, i+1, end, cuts+1)){
                    return true;
                }
            }
        }

    }
    bool isParlidrome(const string &str, int start, int end){
        int l = start;
        int r = end;
        if (memo.count(pair(start, end)) != 0) {
            return memo[pair(start,end)];
        }
        bool is = true;
        while (l < r) {
            if (str[l] != str[r]){
                is = false;
                break;
            }
        }
        memo[pair(start, end)] = true;
        return is;
    }

};
//---------------------------
void main() {
    printIfComb(0, 0, 3);
}
void printIfComb(string &res, int open, int close, int total) {
    if (close == total) { 
        printf("%s \n", res.c_str()); 
        return; 
    }
    if (close < open) {
        string new_res = res + spaces(close) + "}";
        printIfComb(new_res, open, close+1; total);
    }
    if (open < total) {
        new_res = res + "if {" + spaces(open);
        printIfComb(new_res, open+1, close, total);
    }

    string spaces(int n) {
        string res = "";
        for (int i=0; i<2*n; i++){
            res += " ";
        }
        return res;
    }
}