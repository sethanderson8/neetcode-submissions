class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                cur_length = 1
                while (num + 1) in nums_set:
                    cur_length += 1
                    num += 1

                longest = max(longest, cur_length)
            
        return longest