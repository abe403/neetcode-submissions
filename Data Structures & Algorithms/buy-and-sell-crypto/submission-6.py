class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l + 1

        best = 0

        # [0,1,2,3,4,5]

        # [1,2,3,4,5]
        # 5

        while l < r and r <= len(prices) - 1:

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                best = max(best, profit)
            else:
                l = r
            
            r += 1
        
        return best

            
