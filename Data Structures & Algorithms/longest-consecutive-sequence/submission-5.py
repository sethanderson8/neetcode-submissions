class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # HashSet where we are looking if we have num - 1 in it
        # We can go over the array, input our value, do a loop to check if num - 1 is in set
        # Would need two for loops to go over the nums first then do this to figure out the longest

        uniqueNums = set(nums)
        longestConsecutive = 0

        for num in uniqueNums:
            if num + 1 not in uniqueNums:
                currentConsecutive = 1
                prevNum = num - 1
                while prevNum in uniqueNums:
                    currentConsecutive += 1
                    prevNum -= 1

                longestConsecutive = max(longestConsecutive, currentConsecutive)

        return longestConsecutive

        