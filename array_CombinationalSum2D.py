
#row_sums = [4, 4, 4]
#col_sums = [4, 4, 4]
row_sums = [2, 2]
col_sums = [4]

n_rows = len(row_sums)
n_cols = len(col_sums)

def gen_matrix(matrix, r, c, cur_col_sum, cur_row_sum):
    if c == n_cols:
        if cur_row_sum == row_sums[r]:
            if r == n_rows-1:
                print("Generated Matrix:", matrix)
                return
            else:
                cur_row_sum = 0
                gen_matrix(matrix, r+1, 0, cur_col_sum, cur_row_sum)
    else:
        left = min(row_sums[r] - cur_row_sum, col_sums[c] - cur_col_sum[c])
        for i in range(left+1):
            matrix[r][c] = i
            cur_row_sum += i
            cur_col_sum[c] += i
            if r != n_rows - 1 or cur_col_sum[c] == col_sums[c]:
                gen_matrix(matrix, r, c+1, cur_col_sum, cur_row_sum)
            cur_row_sum -= i
            cur_col_sum[c] -= i
            
cur_col_sum = [0] * n_cols
matrix = [[0] * n_cols for _ in range(n_rows)]
gen_matrix(matrix, 0, 0, cur_col_sum, 0)
