# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.sum(root, 0)
        else:
            return 0

    def sum(self, root, _sum):
        _sum += root.val
        if not root.left and not root.right:
            return _sum
        _sum *= 10
        if root.left and not root.right:
            return self.sum(root.left, _sum)
        elif not root.left and root.right:
            return self.sum(root.right, _sum)
        else:
            return self.sum(root.left, _sum) + self.sum(root.right, _sum)
