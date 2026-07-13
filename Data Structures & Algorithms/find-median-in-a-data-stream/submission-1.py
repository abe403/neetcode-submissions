class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    # 1,2,3,4

    def findMedian(self) -> float:
        
        n = len(self.nums)
        
        l = sorted(self.nums)
        h = n // 2
        if n % 2 == 1:
            return l[h]
        else:
            return (l[h] + l[h-1]) / 2