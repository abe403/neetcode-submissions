class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        leftProduct = []

        rightProduct = []

        lsum = 1

        for n in nums:
            leftProduct.append(lsum)
            lsum *= n
        
        rsum = 1

        for i in range(len(nums)-1, -1, -1):
            rightProduct.insert(0, rsum)
            rsum *= nums[i]
        
        for i in range(len(nums)):
            output[i] = leftProduct[i] * rightProduct[i]
        
        return output