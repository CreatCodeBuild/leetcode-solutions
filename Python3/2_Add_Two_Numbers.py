# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def go_through(node):
	yield node.val
	if node.next is not None:
		yield from go_through(node.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        g1 = go_through(L1)
        g2 = go_through(L2)
        ret = ListNode(0)
        while True:
        	try:
        		digit1 = next(g1)
				digit2 = next(g2)    
