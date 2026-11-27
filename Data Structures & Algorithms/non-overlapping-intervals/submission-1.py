class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def sol_by_end():
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

        # return sol_by_end()

        def sol_by_start():
            intervals.sort()
            count = 0
            last_end = float('-inf')
            for start, end in intervals:
                if start >= last_end:
                    last_end = end
                else:
                    count += 1
                    last_end = min(end, last_end)
            return count

                    
        return sol_by_start()
