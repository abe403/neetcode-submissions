class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}

        l = 0

        mcc = 0

        for r in range(len(s)):
            
            cur = seen.get(s[r], 0)+1

            seen[s[r]] = cur

            mcc = max(mcc, seen[s[r]])

            while r - l + 1 - mcc > k:
                seen[s[l]] = seen.get(s[l]) - 1
                l += 1

        return r-l+1
            

            
