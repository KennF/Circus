# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def getInt(self, ln):
    	sum = 0
    	i = 0
    	while(ln != None):
    		sum = sum + ((10 ** i) * ln.val)
    		ln = ln.next
    		i = i + 1
    	print "int: " + str(sum)
    	return sum

    def getListNode(self, sum):
    	head = ListNode(sum % 10)
    	pre = head
    	sum = sum / 10
    	while(sum != 0):
    		e = ListNode(sum % 10)
    		sum = sum / 10
    		pre.next = e
    		pre = e	
    	return head

    def addTwoNumbers(self, l1, l2):
    	sum = self.getInt(l1) + self.getInt(l2)
    	return self.getListNode(sum)

    def printListNode(self, l):
    	while(l != None):
    		print str(l.val) + '-->'
    		l = l.next

if __name__ == '__main__':
	e1 = ListNode(2)
	e2 = ListNode(4)
	e3 = ListNode(3)
	e1.next = e2
	e2.next = e3

	a1 = ListNode(5)
	a2 = ListNode(6)
	a3 = ListNode(4)
	a1.next = a2
	a2.next = a3
	s = Solution()
	s.printListNode(e1)
	s.printListNode(a1)
	s.printListNode(s.addTwoNumbers(e1, a1))

	ee1 = ListNode(0)
	ee2 = ListNode(1)

	s = Solution()
	s.printListNode(ee1)
	s.printListNode(ee2)
	s.printListNode(s.addTwoNumbers(ee1, ee2))


	
        