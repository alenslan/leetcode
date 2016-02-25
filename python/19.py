class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 0x7FFFFFFF: return False
        if x < - 0x7FFFFFFF - 1: return False
        x = abs(x)
        strx = str(x)
        if strx == strx[::-1]:
            return True
        return False

S = Solution()

assert False == S.isPalindrome(-2147483648)
assert False == S.isPalindrome(123)
assert True == S.isPalindrome(11)
assert True == S.isPalindrome(-11)
assert False == S.isPalindrome(1534236469)
print S.isPalindrome(-2147447412)
