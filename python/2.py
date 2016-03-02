#coding:utf-8
'''
翻转单向链表
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse(self, L):
        if not L: return None
        
        NL = ListNode('')
        while 1:
            tmp = NL.next
            NL.next = L
            L = L.next
            NL.next.next = tmp
            if not L.next: # 最后个数据放到第一个
                NL.val = L.val
                break
        return NL

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

S = Solution()
res = S.reverse(a)
# print res.val
# print res.next.val
# print res.next.next.val
# print res.next.next.next.val
assert res.val == 4
