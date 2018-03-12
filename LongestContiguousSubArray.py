
"""
Length of the largest subarray with contiguous elements | Set 1
Given an array of distinct integers, find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.

Examples:

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5
"""


def length1(nums):
    max_len = 1
    for i in range(len(nums)-1):
        mn = nums[i]
        mx = nums[i]
        for j in range(i+1, len(nums)):
            mn = min(mn, nums[j])
            mx = max(mx, nums[j])
            if (mx - mn) == j - i:
                max_len = max(max_len, mx - mn + 1)
    return max_len

a = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
#a = [14, 12, 11, 20]

print(length1(a))

