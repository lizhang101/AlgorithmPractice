def length2(nums):

    if len(nums) < 2:
        return len(nums)
    max_len = 1
    cur_len = 1
    nums.sort()
    print(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]-1:
            cur_len += 1
            max_len = max(cur_len, max_len)
        else:
            cur_len = 1
    return max_len

a = [1, 3, 2, 4]

print(length2(a))

