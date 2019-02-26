# https://leetcode.com/problems/range-sum-of-bst
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        
        stack = [root]
        
        while stack:
            
            node = stack.pop()
        
            if L <= node.val <= R:
                sum += node.val

            if node.val > L and node.left is not None:
                stack.append(node.left)
            if node.val < R and node.right is not None:
                stack.append(node.right)
        
        return sum
