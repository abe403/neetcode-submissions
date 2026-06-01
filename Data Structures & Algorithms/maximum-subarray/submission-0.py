class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best = nums[0]
        count = 0

        for num in nums:
            count += num
            best = max(count, best)

            if count < 0:
                count = 0
        
        return best

