class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        given intervals
        remove some to make it non-overlapping
        don't know about sort

        sort by end
        iterate and pick max intervals => min discarded
        """

        intervals.sort(key=lambda key: key[1])
        count = 0
        last_end = float('-inf')
        for interval in intervals:
            if interval[0] < last_end:
                count += 1
            else:
                last_end = max(last_end, interval[1])
        
        return count
