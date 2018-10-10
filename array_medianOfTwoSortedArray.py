def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    if not nums1 and not nums2:
        return 0.0

    m = len(nums1)
    n = len(nums2)
    isOdd = True if (m + n) % 2 else False

    if m > n:
        m, n = n, m
        nums1, nums2 = nums2, nums1

    l = 0
    r = m - 1
    half = (m + n) // 2
    while l <= r:
        i = (l + r) // 2
        j = half - i
        if i > 0 and nums1[i - 1] >= nums2[j]:
            r = i - 1
        elif j > 0 and nums2[j - 1] >= nums1[i]:
            l = i + 1
        else:
    max_left = max(nums1[i - 1], nums2[j - 1])
    min_right = min(nums1[i], nums2[j])
    if isOdd:
        return max_left if (i + j) > half else min_right
    else:
        return (max_left + min_right) / 2.0

nums1 = [1, 2]
nums2 = [1, 1]
print(findMedianSortedArrays(nums1, nums2))