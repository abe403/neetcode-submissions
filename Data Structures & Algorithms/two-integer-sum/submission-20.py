class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            comp = target - nums[i] 
            seen[comp] = i
        
        for i in range(len(nums)):
            if nums[i] in seen:
                if seen[nums[i]] == i:
                    continue
                res = [i, seen[nums[i]]]
                res.sort()
                return res
