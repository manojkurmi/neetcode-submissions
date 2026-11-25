"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda a: a.start)

        last_end = 0
        for interval in intervals:
            if interval.start < last_end:
                return False
            last_end = max(last_end, interval.end)

        return True
