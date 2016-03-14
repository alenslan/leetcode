#coding:utf-8
"""
找出一个列表非负整数的数字表示的单线柱子的高
方法就是找出两个相间能装最多水的地方 ,取 4， 3的段个各自能装最多的水
例子 [4, 2, 3]
|
|     |
|  |  |
|  |  |
-------------------->
x
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 2: return 0
        
        l, r = 0, len(height) - 1
        res = 0
        #逆向扫描
        for i in range(len(height) - 1, 0 , -1):
            if height[l] < height[r]:
                res, l = max(res, height[l] * i), l + 1
            else:
                res, r = max(res, height[r] * i), r - 1
        return res

S = Solution()
l1 = [1, 1]
l2 = [2, 1, 3]
l3 = [2, 2, 2, 3]
l4 = [2, 1, 2, 3]
l5 = [2, 1, 2, 1, 3]
assert 1 == S.maxArea(l1)
assert 4 == S.maxArea(l2)
assert 6 == S.maxArea(l3)
assert 6 == S.maxArea(l4)
assert 8 == S.maxArea(l5)
print S.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])