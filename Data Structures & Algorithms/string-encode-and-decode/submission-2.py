class Solution:

    def encode(self, strs: List[str]) -> str:        

        fs = ""

        for s in strs:
            fs += str(len(s)) + "#" + s
        return fs

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        while i < len(s):

            hp = s.find("#", i)

            size = int(s[i:hp])

            res.append(s[hp+1:hp+1+size])

            i = hp+1+size

        return res

