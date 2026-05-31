class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = [0] * 26

        keys = {}

        res = []

        for s in strs:
            for c in s:
                pos = ord('a') - ord(c)
                freq[pos] += 1
            st = ""
            for v in freq:
                st += str(v)
            keys.setdefault(st, [])
            keys[st].append(s)
            freq = [0] * 26
        
        for k in keys:
            res.append(keys[k])
        return res


