class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        merge all overlapping
        same end and start is overlapping
        no indication for sorted
        """
        # sort
        # iterate and merge

        intervals.sort()
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res