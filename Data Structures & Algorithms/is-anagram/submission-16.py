class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lfreq = {}
        rfreq = {}

        for c in s:
            lfreq[c] = lfreq.get(c, 0) + 1
        
        for c in t:
            rfreq[c] = rfreq.get(c, 0) + 1

        return lfreq == rfreq