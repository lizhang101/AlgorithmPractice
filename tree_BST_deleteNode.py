# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def deleteTree(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    if root is None:
      return root
    else:
      if key > root.val:
        root.right = self.deleteTree(root.right, key)
        return root
      elif key < root.val:
        root.left = self.deleteTree(root.left, key)
        return root
      else:
        if root.right is None:
          return root.left
        elif root.left is None:
          return root.right
        else:
          pre = root.right
          successor = root.right
          while successor and successor.left:
            pre = successor
            successor = successor.left
            root.right = successor.right
          pre.left = successor.right
          successor.left = root.left
          return successor