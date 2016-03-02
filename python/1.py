#coding:utf-8
'''
冒泡排序python实现
a1, a2比较，如果a1 > a2则 a2和a1位置互换，直到下一轮再比较
'''
class Solution(object):
    def bubble_sort(self, L1):
        l = len(L1)
        for i in range(l):
            for j in range(i, l):
                if L1[i] > L1[j]:
                    L1[i], L1[j] = L1[j], L1[i]
        return L1

a = [6, 2, 4, 1, 5, 9]

S = Solution()
b = S.bubble_sort(a)
print b
assert [1, 2, 4, 5, 6, 9] == b