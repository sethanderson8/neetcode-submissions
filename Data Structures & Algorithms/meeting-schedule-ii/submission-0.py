"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_rooms = 0
        # sort by start time first
        intervals.sort(key=lambda interval: interval.start)

        # Overlap heap that just stores the end times sorting by that
        overlap_heap = []
        for interv in intervals:
            # only do comparisons when the overlap heap is not None
            # while our current meeting's start is greater than or equal to 
            # the top of heaps end time, we pop
            while overlap_heap and interv.start >= overlap_heap[0]:
                heapq.heappop(overlap_heap)

            # no matter what, we will be pushing our current meeting end to the overlap heap
            heapq.heappush(overlap_heap, interv.end)

            min_rooms = max(min_rooms, len(overlap_heap))

        return min_rooms

        # they are conflicting if there is an overlap. Each time there is an overlap, we need
        # at least one additional room at that time. If more than 2 overlap, the total numbers of
        # rooms needs is the number of overlaps that can occur at any point in time at the
        # same time. We will be taking the max of the overlaps and returning that

        # Intervals are overlapping when i2[1] > i1[0] and i2[0] < i1[1]

        # to do this in a single pass we need to sort on start times
        # start with initial meeting, then check if next meeting overlaps
        # if so, increment min rooms. store the current overlap period, then
        # go to the next meeting. If the next meetings start time is greater than or
        # equal to our lowest seen meeting's end time, we get rid of those meetings
        # whose end times are lower than the current meetings start time
            # they are not overlapping
        
        # If overlapping with our current overlap period, increment again
        # once we find a meeting that is not overlapping with our current overlap period, we 
        # can 

        # [(0,40),(5,10),(15,20), (7, 12), (16,18), (17,19)]
        # sorted by start: [(0,40),(5,10),(7, 12),(15,20),(16,18), (17,19)]
        # overlaps (sorted by end): [(5,10),(7, 12),(0,40)] now (15,20)
            # max is 3 rn
        # pop off the heap until we are overlapping again OR its empty
        # overlaps (sorted by end): [(0,40)] now (15,20) -> [(15,20),(0,40)]
            # max is still 3 since overlaps is only 2 rn
        # now for (16,18), (17,19) add to heap each
            # [(16,18),(15,20),(0,40)] -> [(16,18),(17,19),(15,20),(0,40)] 
        # heap size is 4 so max is updated to 4 here.