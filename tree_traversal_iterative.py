from tree_serialize import *


def preorderTreeRecur(res, root):
    if root is None:
        return
    res.append(root.val)
    preorderTreeRecur(res, root.left)
    preorderTreeRecur(res, root.right)

def preorderTree(root):
    queue = [root]
    cur = None
    res = []
    while queue or cur:
        if cur:
            res.append(cur.val)
            queue.append(cur.right)
            queue.append(cur.left)
        if queue:
            cur = queue.pop(-1)

    return res


def inorderTree(root):
    queue = []
    cur = root
    res = []
    while queue or cur:
        while cur:
            queue.append(cur)
            cur = cur.left
        cur = queue.pop(-1)
        res.append(cur.val)
        if cur.right:
            cur = cur.right
        else:
            cur = None
    return res




def postorderTree(root):
    queue = []
    cur = root
    res = []
    while queue or cur:
        while cur:
            queue.append(cur)
            cur = cur.left
        cur = queue[-1]
        if cur.right:
            cur = cur.right
        else:
            res.append(cur.val)
            queue.pop(-1)
            cur = None
    return res


if __name__ == "__main__":
    root = deserializeTree("1 2 3 4 5 6 7")
    arr = []
    preorderTreeRecur(arr, root)
    print(arr)
    arr = preorderTree(root)
    print(arr)
    arr = inorderTree(root)
    print(arr)
    arr = postorderTree(root)
    print(arr)
