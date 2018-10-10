import utili
def serializeTree(root):
    def serializeHelper(node):
        if not node:
            vals.append('#')
            return
        vals.append(str(node.val))
        serializeHelper(node.left)
        serializeHelper(node.right)
    vals = []
    serializeHelper(root)
    return ' '.join(vals)

def deserializeTree(head):


    def deserializeHelper():
        try:
            val = next(vals)
            if val == '#':
                return None
        except StopIteration:
            return None
        node = utili.TreeNode(int(val))
        node.left = deserializeHelper()
        node.right = deserializeHelper()
        return node

    def isplit(source, sep):
        sepsize = len(sep)
        start = 0
        while True:
            idx = source.find(sep, start)
            if idx == -1:
                yield source[start:]
                return
            yield source[start:idx]
            start = idx + sepsize
    vals = iter(isplit(head, ' '))

    return deserializeHelper()

if __name__ == "__main__" :
    root = deserializeTree("1 # 2 # #")
    head = serializeTree(root)
    print (head)
