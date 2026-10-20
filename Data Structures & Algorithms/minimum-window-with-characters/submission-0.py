class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ss = ""

        count = {}

        min_len = 987654

        have = 0

        l = 0
        r = 0

        for c in t:
            count[c] = count.get(c, 0) + 1
        
        win_count = {}

        while r < len(s):

            win_count[s[r]] = (win_count.get(s[r], 0) + 1)

            if win_count.get(s[r], 0) == count.get(s[r], 0):
                have += 1
            
            while have == len(count):
                if (r - l + 1) < min_len:
                    ss = s[l:r+1]
                    min_len = (r - l + 1)
                
                win_count[s[l]] = win_count.get(s[l], 0) - 1
                

                if win_count.get(s[l], 0) < count.get(s[l], 0):
                    have -= 1

                l += 1

            r += 1
            
        return ss
                
            



