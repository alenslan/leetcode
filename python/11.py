#coding:utf-8
class Solution(object):
    '''
    显示列表里相加等于一个给定值的索引
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p = {}
        for i, y in enumerate(nums):
            if p.get(target - y):
                return [p.get(target - y), i + 1]
            else:
                p[y] = i + 1


s = Solution()
print s.twoSum([2,7,11,15], 9)