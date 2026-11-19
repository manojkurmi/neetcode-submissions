from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-val, key) for key, val in freq.items()]
        heapify(heap)
        res = []

        for _ in range(k):
            val, key = heappop(heap)
            res.append(key)
        
        return res
