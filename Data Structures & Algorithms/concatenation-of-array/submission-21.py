class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # get length bc it is will be fixed if we do it before
        initial_len_nums = len(nums)
        for i in range(0, initial_len_nums):
            nums.append(nums[i])

        return nums