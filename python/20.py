#coding:utf-8
'''
去掉重复的字母，使用lexicographical order找出最短的字串
'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = {x:i for i, x in enumerate(s)}
        res = ''
        for j, y in enumerate(s):
            if y not in res:
                while y < res[-1:] and j < rs[res[-1]]:
                    res = res[:-1]
                res += y
        return res


S = Solution()
s1 = 'bcabc'
s2 = 'cbacdcbc'

assert 'abc' == S.removeDuplicateLetters(s1)
assert 'acdb' == S.removeDuplicateLetters(s2)