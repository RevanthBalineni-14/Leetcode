import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 =nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        lo, hi = 0, n1
        while lo<=hi:
            cut1 = (lo+hi)//2
            cut2 = (n1+n2)//2 - cut1
            l1 = nums1[cut1-1] if cut1!=0 else float(-inf)
            l2 = nums2[cut2-1] if cut2!=0 else float(-inf)
            r1 = nums1[cut1] if cut1<n1 else float(inf)
            r2 = nums2[cut2] if cut2<n2 else float(inf)
            
            if(l1>r2):
                hi = cut1-1
            elif(l2>r1):
                lo = cut1+1
            else:
                if (n1+n2)%2 == 0: return (max(l1,l2)+min(r1,r2))/2
                else: return min(r1,r2)