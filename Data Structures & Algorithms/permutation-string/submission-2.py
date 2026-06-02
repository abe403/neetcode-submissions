class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1s = sorted(s1)

        for i in range(0, len(s2) - len(s1) + 1, 1):

            if s1s == sorted(s2[i:i+len(s1):1]):
                return True
        
        return False