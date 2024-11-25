import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        if(len(a)%2==0):
            h = int(len(a)/2)
            l = a[h-1] + a[h]
            x = l/2
        else:
            h = int(len(a)/2)
            x = a[h]
        return x        

