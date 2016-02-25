#coding:utf-8
'''
折半查找法双排序列表的中位数
'''
def half_find(l1, d):
    if len(l1) == 0: return
    if len(l1) == 1:
        if l1[0] == d:
            return d
        else:
            return
    if d < l1[0]: return 
    if d > l1[-1]: return
    
    mid = len(l1) / 2
    if l1[mid] == d:
        return d
    if l1[mid] < d:
        return half_find(l1[mid+1:], d)
    else:
        return half_find(l1[0:mid], d)

    return

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def media(l1, l2, k):
            m = len(l1)
            n = len(l2)
            if m > n:
                l1, l2 = l2, l1

            if not l1: return l2[k]
            if k + 1 == m + n:
                return l1[-1] if l1[-1] > l2[-1] else l2[-1]
                
            c = len(l1) / 2
            t = k - c

            if l1[c] > l2[t]:
                return media(l1[:c], l2[t:], c)
            else:
                return media(l1[c:], l2[:t], t)
                
        l = len(nums1) + len(nums2)
        k = l / 2
        if l & 0x10:
            return media(nums1, nums2, k)
        else:
            return (media(nums1, nums2, k - 1) + media(nums1, nums2, k)) / 2.0
                   
def media_array(l1, l2, k):
    
    # 检验空数据输入
    if len(l1) > len(l2):
        l1, l2 = l2, l1

    if not l1: return l2[k]
    if len(l1) == 1:
        return max(l1[-1], l2[-1])
        
    c = len(l1) // 2
    t = k - c

    if l1[c] > l2[t]:
        return media_array(l1[:c], l2[t:], c)
    else:
        return media_array(l1[c:], l2[:t], t)

def main(l1, l2):
    l = len(l1) + len(l2)

    if l % 2:
        return media_array(l1, l2, l // 2)
    else:
        return (media_array(l1, l2, l // 2 - 1) + media_array(l1, l2, l // 2)) / 2.0

l1 = [1, 1, 1]
l2 = [1, 1, 1]

C = Solution()
print C.findMedianSortedArrays(l1, l2)
