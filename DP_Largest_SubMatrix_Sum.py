import sys
class Solution(object):
    def largest(self, matrix):
        """
        input: int[][] matrix
        return: int
        """
        # write your solution here
        col_sum = [0] * len(matrix[0])
        max_sum = -sys.maxsize
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #print( matrix_sum[j] + left_sum + col_sum[j] + matrix[i][j] )
                col_sum[j] = max(col_sum[j] + matrix[i][j], matrix[i][j])
                if j == 0:
                    max_sum = max(max_sum, col_sum[0])
                else:
                    max_sum = max(max_sum, col_sum[j-1]+col_sum[j])
            print("col:", col_sum)
        return max_sum

sol = Solution()
input = [[2, -1, 2, 1, -3],
         [0, -2, -1, 2, 1],
         [3, 2, 1, -3, -2]]
print(sol.largest(input))