class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""

        res = ""
        
        for t, value in self.store[key]:
            if t <= timestamp:
                res = value
            else:
                break
        
        return res
