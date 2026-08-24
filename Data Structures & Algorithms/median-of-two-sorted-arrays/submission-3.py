class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1i = 0
        n2i = 0

        sA = []

        while n1i < len(nums1) and n2i < len(nums2):
            if nums1[n1i] < nums2[n2i]:
                sA.append(nums1[n1i])
                n1i += 1
            else:
                sA.append(nums2[n2i])
                n2i += 1
        
        while n1i < len(nums1):
            sA.append(nums1[n1i])
            n1i += 1
        
        while n2i < len(nums2):
            sA.append(nums2[n2i])
            n2i += 1
        
        sAl = len(sA)
        
        mid = sAl // 2

        if sAl % 2 == 1:
            return sA[mid]
        else:
            return (sA[mid] + sA[mid - 1] ) / 2

