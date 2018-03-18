#Find the smallest positive integer value that cannot be represented as sum of any subset of a given array
#Input:  arr[] = {1, 3, 6, 10, 11, 15};
#Output: 2

#Input:  arr[] = {1, 1, 1, 1};
#Output: 5

#Input:  arr[] = {1, 1, 3, 4};
#Output: 10

#Input:  arr[] = {1, 2, 5, 10, 20, 40};
#Output: 4

#Input:  arr[] = {1, 2, 3, 4, 5, 6};
#Output: 22

#
def smallest_pnum(nums):
    if nums[0] > 1:
        return 1
    mx = 1
    for n in nums[1:]:
        if n > mx + 1:
            return mx + 1
        mx = n + mx;
    return mx + 1

#arr = [1, 3, 6, 10, 11, 15]
#arr = [1, 1, 1, 1]
#arr = [1, 1, 3, 4]
#arr = [1, 2, 5, 10, 20, 40]
arr = [1, 2, 3, 4, 5, 6]
print(smallest_pnum(arr))


