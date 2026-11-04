class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Compare end time of either interval to see if ones interval is greater than or equal to the start time of the other
        # if true, find the overlap. Need to now store this in an ans. For the next overlap comparison, we increment the interval list with the lower end time
        # if false, they are not overlapping. In this case, you would want to increment the one with the smaller start time to see if now that next interval overlaps with the other comparing interval
        overlaps = []
        i1_ind = 0
        i2_ind = 0

        while i1_ind < len(firstList) and i2_ind < len(secondList):
            if self.are_overlapping(firstList[i1_ind], secondList[i2_ind]):
                # get the overlap, increment the one with the smaller end time
                overlaps.append([max(firstList[i1_ind][0], secondList[i2_ind][0]),
                                min(firstList[i1_ind][1], secondList[i2_ind][1])])
            # in any case, you actually always increment the ind with the smaller end time
            if firstList[i1_ind][1] < secondList[i2_ind][1]:
                i1_ind += 1
            elif firstList[i1_ind][1] > secondList[i2_ind][1]:
                i2_ind += 1
            else:
                # if both are ending are equal spot we can incrememnt both
                i1_ind += 1
                i2_ind += 1

        return overlaps


    def are_overlapping(self, i1, i2) -> bool:
        # if i1 start time is less than i2 end time
        # and i1 end time is greater than i2 start time

        if i1[0] <= i2[1] and i1[1] >= i2[0]:
            return True
        return False