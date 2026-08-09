class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0

        maxLen = 0

        seen = set()

        while r < len(s):

            if s[r] not in seen:
                seen.add(s[r])
                r = r + 1
            else:
                seen.remove(s[l])
                l = l + 1

            maxLen = max(maxLen, len(seen))
        
        return maxLen
            