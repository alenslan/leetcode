#coding:utf-8
'''
Z转换会话
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        sl = len(s)

        if numRows <= 1 or sl < 3 or sl <= numRows: return s
        
        t = 2 * numRows - 2
        s2 = ''
        for x in xrange(numRows):
            if x == 0 or x == numRows - 1:
                for y in xrange(x, sl, t):
                    s2 += s[y]
                continue
                          
            s2 += s[x] # 行首
            for y in xrange(t - x, sl, t):#间隔行的数据
                s2 += s[y]
                if y + 2 * x < sl:
                    s2 += s[y + 2 * x]
        return s2
        
S = Solution()
# assert 'PAHNAPLSIIGYIR' == S.convert('PAYPALISHIRING', 3)
assert 'PINALSIGYAHRPI' == S.convert('PAYPALISHIRING', 4)
#assert 'ABC' == S.convert('ACB', 2)