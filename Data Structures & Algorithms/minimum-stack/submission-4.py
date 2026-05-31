class MinStack:
    
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minval = sys.maxsize
        for n in self.stack:
            minval = min(minval, n)
        return minval
