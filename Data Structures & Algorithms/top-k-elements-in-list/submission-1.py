class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        
        orderedList = []
        res = []

        for n in nums:
            freqs[n] += 1
        


        for n in freqs:
            orderedList.append((n, freqs[n]))
            orderedList.sort(key = lambda p: p[1], reverse = True)
        
        for i in range(k):
            res.append(orderedList[i][0])

        return res