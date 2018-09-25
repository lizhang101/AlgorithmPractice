class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

def genListRand(L):
    import random
    p = dummy = ListNode(0)
    for i in range(L):
        p.next = ListNode(random.randint(1, 100))
        p = p.next
    return dummy.next

def genList(L):
    import random
    p = dummy = ListNode(0)
    for n in L:
        p.next = ListNode(n)
        p = p.next
    return dummy.next

def printList(head):
    i = 0
    while head:
        print("i:{} val:{}".format(i, head.val))
        head = head.next
        i += 1
