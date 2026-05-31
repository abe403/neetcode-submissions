class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        maxArea = 0

        for i in range(0, len(heights), 1):
            l = i - 1
            r = i + 1

            area = heights[i]

            while l >= 0 and heights[l] >= heights[i]:
                area += heights[i]
                l -= 1

            while r <= len(heights) - 1 and heights[r] >= heights[i]:
                area += heights[i]
                r += 1
            
            maxArea = max(maxArea, area)

        return maxArea

