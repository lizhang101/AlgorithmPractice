class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


def genListRand(L):
    """ Generate a singly linked list by L random numbers in a range of 1-100.

    :param L: length of linked list to generate
    :return: head
    """
    import random
    p = dummy = ListNode(0)
    for i in range(L):
        p.next = ListNode(random.randint(1, 100))
        p = p.next
    return dummy.next

def genList(L):
    """ Generate a singly linked list

    :param L: the input list to generate the linked list
    :return: the head to the linked list
    """
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

class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left != None:
            for elem in self.left:
                yield elem

        yield self.val

        if self.right != None:
            for elem in self.right:
                yield elem
class Tree:
    pass

