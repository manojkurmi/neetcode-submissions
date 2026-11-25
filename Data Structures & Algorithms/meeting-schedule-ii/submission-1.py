from heapq import heappush, heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda key:key.start)
        heap = [float('inf')]
        max_len = 1

        for interval in intervals:
            while heap[0] <= interval.start:
                heappop(heap)
            heappush(heap, interval.end)
            max_len = max(max_len, len(heap))
        
        return max_len - 1
