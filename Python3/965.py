# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = every(root)
        first = next(values)
        for v in values:
            if first != v:
                return False
        return True
        
def every(root):
    stack = [root]
    while stack:
        n = stack.pop()
        if n:
            yield n.val
            stack.append(n.left)
            stack.append(n.right)
