import random


#quick sort
def partition(arr, left, right):
    pidx = random.randint(left, right+1)
    arr[-1], arr[pidx] = arr[pidx], arr[-1]
    l = i = left
    r = right-1
    while i < r:
        if arr[i] < arr[-1]:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
            i += 1
        elif arr[i] > arr[-1]:
            arr[r], arr[i] = arr[i], arr[r]
            r -= 1
        else:
            i += 1

    arr[-1], arr[i] = arr[i], arr[-1]
    return i

def quickSort(arr, l, r):
    i = partition(arr, 0, len(arr))
    quickSort(arr, l, i)
    quickSort(arr, i+1, r)

if __name__ == "__main__":
    arr = [5, 3, 2]
    quickSort(arr, 0, len(arr))
    print(arr)
