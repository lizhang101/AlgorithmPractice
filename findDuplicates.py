def findDuplicates(arr, n):
    print("input:", arr)
    
    fast = slow = arr[0]
    while True:  #fast < len(arr) and slow < len(arr): if Guaranteed a loop, no need to check the end
        slow = arr[slow + 1]
        fast = arr[arr[fast + 1] + 1]
        if fast == slow:
            break
    
    ptr = arr[0]
    while slow != ptr:
        slow = arr[slow + 1]
        ptr = arr[ptr + 1]
        
    return arr[ptr]
    

print("-----Specified Test Case------")
A = [0, 1, 2, 2, 3, 3, 4]
print("Found duplicate: ", findDuplicates(A, 5))

print("-----Random Test Cases-----")
from random import randint
from random import sample


for i in range(10):
    N = randint(2, 16)
    arr = [randint(0, N-2) for i in range(N)]
    print("Found duplicate: ", findDuplicates(arr, N))
