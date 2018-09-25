import utili
#find the middle node, if the length is even, return the first one

def findMiddleFirst(head):
    if head is None or head.next is None:
        return head

    p0 = p1 = head
    while p0 and p0.next and p0.next.next:
        p0 = p0.next.next
        p1 = p1.next

    print(p1.val)

    return p1

#return the second middle node
def findMiddleSecond(head):
    if head is None or head.next is None:
        return head

    p0 = p1 = head
    while p0 and p0.next:
        p0 = p0.next.next
        p1 = p1.next

    print(p1.val)

    return p1




head = utili.genList(list(range(1, 9)))
utili.printList(head)
findMiddleFirst(head)
findMiddleSecond(head)
