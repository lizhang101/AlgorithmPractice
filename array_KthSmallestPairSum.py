
def KthSmallestPairSum(A, B, K):
    pos = [0] * len(B)
    k = 0
    while k < K:
        temp, ind = B[0] + A[pos[0]], 0
        #print(pos)
        for i in range(1, len(B)):
            if pos[i] < pos[i - 1]:
                S = B[i] + A[pos[i]]
                #print(i, S)
                if S < temp:
                    temp = S
                    ind = i
            if pos[i] == pos[i - 1] == 0:
                break
        print(k, ': ', B[ind], A[pos[ind]], temp)
        pos[ind] += 1
        k += 1
    return temp

A = [1, 2, 5, 9, 10]
B = [5, 8, 10, 11, 13]
K = 10
KthSmallestPairSum(A, B, K)
