class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # When an intervals end time is greater than or equal to another
        # intervals start time, you can merge them.
        # Merge - you take the lower start time of the two and higher
        # end time of the two

        # if you sorted the intervals by start time, you could go through in one
        # pass
        # Merge starting from the first interval, if it is a new interval, you
        # keep using that one to merge, if it is not a new interval, you take the
        # next interval you tried to merge with but could not and use that as 
        # your merge interval

        intervals.sort(key=lambda interval: interval[0])
        merged_intervals = []
        merger_interval = intervals[0]
        for i in range(1, len(intervals)):
            if self.can_merge_intervals(merger_interval, intervals[i]):
                merger_interval = self.merge_intervals(merger_interval, intervals[i])
            else:
                # We need to add our full merged interval to the merged_intervals
                # Then make our non mergable interval to our merger interval
                merged_intervals.append(merger_interval)
                merger_interval = intervals[i]

        # Once this for loop is complete, we still have not added our last merger
        # interval to our merged intervals, lets do that
        merged_intervals.append(merger_interval)
        return merged_intervals

    def can_merge_intervals(self, i1: List[int], i2: List[int]) -> bool:
        return i1[1] >= i2[0]

    def merge_intervals(self, i1: List[int], i2: List[int]) -> List[int]:
        return [i1[0], max(i1[1], i2[1])]