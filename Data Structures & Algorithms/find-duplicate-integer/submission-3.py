class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        low, high = 1, len(nums) - 1

        while low < high:

            mid = low + (high - low) // 2

            lessOrEqual = 0

            for num in nums:
                if num <= mid:
                    lessOrEqual += 1
            
            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid
        
        return low