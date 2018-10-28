def sort_stack (stack1):
    """
    input : int[] stack1
    return : No need to return, store result in stack1
    """
    stack2 = []
    stack3 = []
    
    # write your solution here
    def quicksort (nums, n, stack_lt, stack_ge,step):
        print (step, " input:", nums, n, "lt:", stack_lt, "ge:", stack_ge)
        if n <= 1:
            return
        p = nums.pop()
        ge = lt = 0
        stack_ge.append(p)
        ge += 1
        for _ in range(n - 1):
            t = nums.pop()
            if t >= p:
                stack_ge.append(t)
                ge += 1
            else:
                stack_lt.append(t)
                lt += 1

        print(step, " stack_lt ", stack_lt, lt)
        print(step, " stack_ge ", stack_ge, ge)
        quicksort(stack_lt, lt, nums, stack_ge, "less")
        quicksort(stack_ge, ge, stack_lt, nums, "greater")
        
        print("after")
        print(step, " stack_lt ", stack_lt, lt)
        print(step, " stack_ge ", stack_ge, ge)
        for _ in range(lt):
            stack_ge.append(stack_lt.pop())
        for _ in range(lt):
            nums.append(stack_ge.pop())
            
        for _ in range(ge):
            stack_lt.append(stack_ge.pop())
        for _ in range(ge):
            nums.append(stack_lt.pop())
            
        print(step, " output ", nums)
    
    quicksort(stack1, len(stack1), stack2, stack3, "origin")

#stack1 = [1, 2, 3, 4]
#stack1 = [4, 3, 2, 1]
#stack1 = [2, 1, 4, 3]
#stack1 = [2, 1]
sort_stack(stack1)
print(stack1)