class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        scount = {}
        tcount = {}

        for c in s:
            scount[c] = scount.get(c, 0) + 1
        
        for c in t:
            tcount[c] = tcount.get(c, 0) + 1
        
        return scount == tcount