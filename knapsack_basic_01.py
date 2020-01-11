values = [100, 60, 120]
weights = [20, 10, 30]
W = 50

def GetMaxValue(values, weights, W):
    dp = [[0] * (W+1) for _ in range(len(values)+1)]
    
    for i in range(1, len(values)+1):
        for w in range(1, W+1):
            d = w - weights[i-1]
            if d >= 0:
                dp[i][w] = max(dp[i-1][w], dp[i-1][d] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[-1][-1]
    
    
    

print(GetMaxValue(values, weights, W))