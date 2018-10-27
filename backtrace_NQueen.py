def nqueens(n):
    """
    input: int n
    return: int[][]
    """
    # write your solution here
    memo_col = {}
    memo_d = {}

    def gen_pos(output, cur, memo_col, memo_d, i, n):
        if i == n:
            output.append(cur[:])
            return
        else:
            for k in range(n):
                d0 = i - k
                d1 = i + k
                if memo_d.get((1, d0), True) and memo_d.get((-1, d1), True) and memo_col.get(k, True):
                    memo_d[(1, d0)] = False
                    memo_d[(-1, d1)] = False
                    memo_col[k] = False
                    #print (i, k, memo_d, memo_col)
                    gen_pos(output, cur + [k], memo_col, memo_d, i + 1, n)
                    del memo_d[(1, d0)]
                    del memo_d[(-1, d1)]
                    del memo_col[k]
                    #print (i, k, memo_d, memo_col)

    ans = []
    gen_pos(ans, [], memo_col, memo_d, 0, n)
    return ans

print(nqueens(4))