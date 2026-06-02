class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0

        best = 0

        while r < len(s):

            while s[r] in s[l:r]:
                l += 1
            
            best = max(best, r - l + 1)

            r += 1

        return best