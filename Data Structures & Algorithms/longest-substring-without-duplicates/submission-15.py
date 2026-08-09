class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 1

        maxLen = 0

        while l < len(s) and r < len(s):

            if s[r] not in s[l:r]:
                r = r + 1
            else:
                l = l + 1

            maxLen = max(maxLen, len(s[l:r]))
        
        return maxLen
            