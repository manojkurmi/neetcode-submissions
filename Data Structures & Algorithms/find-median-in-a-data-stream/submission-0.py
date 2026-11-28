from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.n = 0
        

    def addNum(self, num: int) -> None:
        """
        left side is max heap
        right side is min heap
        add to smaller heap
        swap the root if all maxheap is not less that all minheap
        """
        self.n += 1
        if len(self.maxheap) == len(self.minheap):
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)
        
        if self.n < 2:
            return
        # swap roots accordingly
        if -self.maxheap[0] > self.minheap[0]:
            left = -heappop(self.maxheap)
            right = heappop(self.minheap)
            heappush(self.maxheap, -right)
            heappush(self.minheap, left)

        
        

    def findMedian(self) -> float:
        if self.n == 0:
            return None
        if (self.n % 2) == 1:
            return -self.maxheap[0]
        
        return (-self.maxheap[0] + (self.minheap[0])) / 2
        
        
    """
    maintain two heap of same size and cal the median accordingly
    """
    