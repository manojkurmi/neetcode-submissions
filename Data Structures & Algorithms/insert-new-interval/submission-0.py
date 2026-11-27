class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][0] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])

        for interval in intervals:
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res


            