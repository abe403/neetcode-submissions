class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1

        minval = 0
        best = 0
        # 3, 5, 1, 10
        while r < len(prices):

            if prices[r] < prices[l]:
                l = r
            else:
                best = max(best, prices[r] - prices[l])
            
            r = r + 1
        
        return best