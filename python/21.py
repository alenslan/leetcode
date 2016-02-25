#coding:utf-8
"""
给定一个LIST包含n个整数，找到里面的a,b,c 使得 a + b + c = 0，找出不重复的3个组合
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #判断空 或者 数据不足
        if not nums or len(nums) < 3: return []

        nums = sorted(nums)
        
        l = len(nums)
        res = []
        for i in range(l):
            t = 0 - nums[i]

            j, k = i + 1, l - 1
            while j < k:
                if (nums[j] + nums[k]) == t:
                    v = [nums[i], nums[j], nums[k]]
                    if v not in res:
                        res.append(v)
                    j += 1
                    k -= 1
                elif (nums[j] + nums[k] < t):
                    j += 1
                else:
                    k -= 1
        return res

S = Solution()
a = [-1, 0, 1, 2, -1, -4]
print S.threeSum(a)