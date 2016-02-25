#coding:utf-8
"""
string 2 int
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str: return 0
        if str in ['', '-', '+']: return 0
        v, p = 0, ''
        for i, x in enumerate(str):
            if x == '' or x == ' ':
                break
            if x in ['-', '+']:
                p += x
            elif ord(x) >= 48 and ord(x) <= 57:
                v = v * 10 + ord(x) - ord('0')
            else:
                break
        if len(p) >= 2: return 0
        if p == '-': v = -v
        res = v
        if res > 0x7FFFFFFF: return 0x7FFFFFFF
        if res < - 0x7FFFFFFF - 1: return -0x7FFFFFFF - 1
        return res


S = Solution()
assert -10 == S.myAtoi('-10')
assert 10 == S.myAtoi('010')
assert 0 == S.myAtoi('-abc')
assert 0 == S.myAtoi('+-2')
assert - 2**31 == S.myAtoi('-2147483649')