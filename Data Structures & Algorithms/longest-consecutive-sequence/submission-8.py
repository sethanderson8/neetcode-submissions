class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            # we do this check to make sure we are checking the 1 in 1,2,3,4 and not
            # wasting time doing the search if it is 2,3, or 4
            if num - 1 not in nums_set:
                cur_length = 1
                while (num + 1) in nums_set:
                    cur_length += 1
                    num += 1

                longest = max(longest, cur_length)
            
        return longest