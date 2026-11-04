"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        elif len(intervals) == 1:
            return 1

        starts = []
        ends = []

        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)

        starts.sort()
        ends.sort()

        ptr_start, ptr_end = 0, 0
        result, count = 0, 0

        for i in range(len(starts)):
            if starts[ptr_start] < ends[ptr_end]:
                ptr_start += 1
                count += 1
            else:
                count -= 1
                ptr_end += 1

            result = max(result, count)

        return result




        
        