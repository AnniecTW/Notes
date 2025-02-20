class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        n = 0
        current = intervals[0]

        for interval in intervals[1:]:
            if interval[0] < current[1]:
                n += 1
                current = min(current, interval, key=lambda x: x[1])
            else:
                current = interval
        return n
