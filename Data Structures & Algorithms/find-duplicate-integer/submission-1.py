class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = [0] * len(nums)

        for num in nums:
            if not seen[num - 1]:
                seen[num - 1] = 1
            else:
                return num
        
        return -1

            