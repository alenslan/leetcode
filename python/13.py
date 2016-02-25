class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        t, m, n = {}, 0, 0
        for i, y in enumerate(s):
            if y in t:
                m = max(m, i - n)
                n = max(n, t[y] + 1)
            t[y] = i
            print t, m, n, len(s) - n
        return max(m, len(s) - n)

S = Solution()

a = 'aab'
print S.lengthOfLongestSubstring(a)
assert 2 == S.lengthOfLongestSubstring(a)


