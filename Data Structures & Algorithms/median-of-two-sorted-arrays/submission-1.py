class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)

        na = nums1 + nums2
        na.sort()

        nal = len(na)

        # [1, 2, 3, 4, 5]

        if nal == 0:
            res = 0
        elif nal == 1:
            res = na[0]
        elif nal % 2 == 0:
            res = (na[nal//2 - 1] + na[(nal//2)]) / 2
        elif nal % 2 == 1:
            res = na[(nal-1)//2]
        return res