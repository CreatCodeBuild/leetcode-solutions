# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Concurrent Design != Concurrent Implementation
并发设计 != 并发实现
'''
class Bad_Design:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        if p is q:
            return True
        
        if p is None and q is not None:
            return False
        
        if p is not None and q is None:
            return False
        
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        return True

# A Good Design with generator feature support
class Good_Design:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        
        iter_p = iterable(p)
        iter_q = iterable(q)
        
        for val in iter_p:
            q_v = next(iter_q)
            if val != q_v:
                return False
        
        return True

def iterable(p):
    if p is None:
        yield p
        return
    else:
        yield p.val
    yield from iterable(p.left)
    yield from iterable(p.right)

# A Good Design without generator feature support
class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':  # policy, action, target
        iter_p = Iterable(p)
        iter_q = Iterable(q)
        
        try:
            while True:
                p_v = iter_p.next()
                q_v = iter_q.next()
                if p_v != q_v:
                    return False
        except:
            return True

class Iterable:
    
    def __init__(self, p):
        self.p = p
        self.stack = [p]
        
    def next(self):
        if not self.stack:
            raise StopIteration()
        top = self.stack.pop()
        if top is None:
            return top
        self.stack.append(top.left)
        self.stack.append(top.right)
        return top.val
