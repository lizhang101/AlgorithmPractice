"""
We have a list of piles of stones, each pile of stones has a certain weight, represented by an array of integers. In each move, we can merge two adjacent piles into one larger pile, the cost is the sum of the weights of the two piles. We merge the piles of stones until we have only one pile left. Determine the minimum total cost.

Assumptions

stones is not null and is length of at least 1
Examples

{4, 3, 3, 4}, the minimum cost is 28

merge first 4 and first 3, cost 7

merge second 3 and second 4, cost 7

merge two 7s, cost 14

total cost = 7 + 7 + 14 = 28
"""

class Solution(object):
    def minCost(self, stones):
        """
        input: int[] stones
        return: int
        """
        # write your solution here
        if len(stones) <= 1:
            return 0
        import sys
        dp = [[sys.maxsize] * (len(stones)) for _ in range(len(stones))]
        for i in range(len(stones)):
            dp[i][i] = 0
        for l in range(2, len(stones) + 1):
            print("----")
            for s in range(len(stones) - l + 1):
                print("s", s, "l", l)
                for i in range(s, s + l-1):
                    print("pre s i e [%d %d %d]"%(s, i, s+l), dp[s][s+l-1])
                    dp[s][s + l - 1] = min(dp[s][s+l-1], dp[s][i] + sum(stones[s:s + l]) + dp[i+1][s+l-1])
                    print("pre s i e [%d %d %d]"%(s, i, s+l), dp[s][s+l-1])

        return dp[0][len(stones)-1]

print(Solution().minCost([4,3,3]))
