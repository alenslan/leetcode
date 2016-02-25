#coding:utf-8
'''
倒转整数
例如
input: 123
output: 321
input: -321
output: -123
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:return x
        y, t, p = 0, 0, 10
        if x < 0:
            t = 1
            x = -x
        while x:
            y = y * p + x % p
            if y > 0x7FFFFFFF: # 最大INT的单位
                return 0
            x = x / p
        return y if not t else -y


S = Solution()
assert 321 == S.reverse(123)
assert -321 == S.reverse(-123)
assert -4321 == S.reverse(-1234)
assert 0 == S.reverse(1534236469) #超过INT的长度的得返回0

print S.reverse(-2147447412)