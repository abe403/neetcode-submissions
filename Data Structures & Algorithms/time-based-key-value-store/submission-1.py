class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timemap:
            return ""
        
        l = 0
        r = len(self.timemap[key]) - 1

        # for v, t in timemap[key]:

        # "alice" = [ ("happy", 2), ("weird", 3), ("sad", 4) ]

        res = ""

        while l <= r:
            
            m = l + (r - l) // 2

            if self.timemap[key][m][1] == timestamp:
                res = self.timemap[key][m][0]
                break

            elif self.timemap[key][m][1] > timestamp:
                r = m - 1
            elif self.timemap[key][m][1] < timestamp:
                res = self.timemap[key][m][0]
                l = m + 1
        
        return res
        