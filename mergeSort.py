def merge(from_array, to_array, i, l):
    k = p0 = i
    p1 = i+l
    end = min(len(from_array), i+2*l)
    while p0 < i+l and p1 < end:
        if from_array[p0] < from_array[p1]:
            to_array[k] = from_array[p0]
            p0 += 1
        else:
            to_array[k] = from_array[p1]
            p1 += 1
        k += 1
    while p0 < i+l:
        to_array[k] = from_array[p0]
        k += 1
        p0 += 1

    while p1 < end:
        to_array[k] = from_array[p1]
        k += 1
        p1 += 1


# Use ping-pong buffer for merging.
# array merge to helper_array, then the other way around
def mergeSortIter(array):
    if not array:
        return
    helper_array = array[:]
    l = 1
    from_array = array
    to_array = helper_array
    while l <= len(array):
        i = 0
        to_array = helper_array if to_array is array else array
        from_array = helper_array if to_array is array else array
        while i + l < len(array):
            merge(from_array, to_array, i, l)
            i += 2*l
        l *= 2
    if to_array is not array:
        array[:] = to_array[:]

# ----recursive version
# first recursively split the array to 2 parts with max diff is no more than 1 in length.
# then merge the 2 parts into one

def merge2(to_array, from_array, l, mid, r):
    k = l
    i = l
    j = mid
    while i < mid and j < r:
        if from_array[i] < from_array[j]:
            to_array[k] = from_array[i]
            i += 1
        else:
            to_array[k] = from_array[j]
            j += 1
        k += 1

    while i < mid:
        to_array[k] = from_array[i]
        i += 1
        k += 1

    while j < r:
        to_array[k] = from_array[j]
        j += 1
        k += 1

def partition(array, helper, l, r):
    if r - l <= 1:
        return
    mid = (l + r)//2
    partition(array, helper, l, mid)
    partition(array, helper, mid, r)
    helper[l:r] = array[l:r]
    merge2(array, helper, l, mid, r)


def mergeSortRecur(array):
    helper_array = [0] * len(array)
    partition(array, helper_array, 0, len(array))
    return


import random
if __name__ == "__main__":
    #arr = random.sample(range(1,100),10)
    arr = [4,3,2,1]
    print(arr)
    #mergeSortIter(arr)
    mergeSortRecur(arr)
    print(arr)
