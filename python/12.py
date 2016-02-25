#coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2 : return None
        
        if not l1: l1 = ListNode(0)

        if not l2: l2 = ListNode(0)

        v = l1.val + l2.val
        p = ListNode(v)
        if v >= 10:
            if not l1.next: l1.next = ListNode(0)
            l1.next.val += 1
            p.val = v % 10
        p.next = self.addTwoNumbers(l1.next, l2.next)
        
        return p


a1 = ListNode(2)
a2 = ListNode(5)

b1 = ListNode(4)
b2 = ListNode(6)

c1 = ListNode(3)
c2 = ListNode(4)

d1 = ListNode(1)
d2 = ListNode(9)

e1 = ListNode(9)

f1 = ListNode(9)

a1.next = b1
b1.next = c1

a2.next = b2
b2.next = c2

d2.next = e1
e1.next = f1

S = Solution()
# d = S.addTwoNumbers(a1,a2)
d = S.addTwoNumbers(d1,d2)
print d.val
print d.next.val
print d.next.next.val
print d.next.next.next.val