class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    p = head
    while p is not None:
        print(p.val)
        p = p.next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def get_mid(head):
            if head is None:
                return None
            pre = fast = slow = head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                pre = slow
                slow = slow.next
            pre.next = None
            return slow

        def merge_sort(head):
            if head is None or head.next is None:
                return head
            #print(head.val)
            mid = get_mid(head)
            p0 = merge_sort(mid)
            p1 = merge_sort(head)
            #print("--p0--")
            #printList(p0)
            #print("--p1--")
            #printList(p1)
            #print (head.val, mid.val)
            p = newhead = ListNode(0)
            while p0 is not None and p1 is not None:
                if p0.val < p1.val:
                    p.next, p0.next, p0 = p0, p1, p0.next
                else:
                    p.next, p1.next, p1 = p1, p0, p1.next
                p = p.next

            if p0 is not None:
                p.next = p0
            elif p1 is not None:
                p.next = p1
            return newhead.next

        return merge_sort(head)
s = Solution()
p = head = ListNode(4)
for v in [3, 1, 2]:
    p.next = ListNode(v)
    p = p.next
h = s.sortList(head)


printList(h)