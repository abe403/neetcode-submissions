class LRUCache:

    def __init__(self, capacity: int):
        self.saved = OrderedDict()
        self.capacity = capacity
        self.lastused = None


    def get(self, key: int) -> int:
        val = self.saved.get(key, -1)

        if val == -1:
            return val
        else:
            self.saved.move_to_end(key)

        return val

    def put(self, key: int, value: int) -> None:

        val = self.saved.get(key)

        if val != None:
            self.saved[key] = value
            self.saved.move_to_end(key)
        else:
            if len(self.saved) < self.capacity:
                self.saved[key] = value
                self.saved.move_to_end(key)
            else:
                self.saved.popitem(last=False)
                self.saved[key] = value
                
        return None