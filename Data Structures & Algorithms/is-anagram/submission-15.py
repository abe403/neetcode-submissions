class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lfreq = {}

        tfreq = {}

        for c in s:
            lfreq[c] = lfreq.get(c, 0) + 1

        for c in t:
            tfreq[c] = tfreq.get(c, 0) + 1

        return lfreq == tfreq
