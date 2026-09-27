class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_val = nums[0]
        low = 1
        slider = 1
        num_unique = 1
        while slider < (len(nums)):
            if prev_val != nums[slider]:
                nums[low] = nums[slider]
                prev_val = nums[low]
                low += 1
                num_unique += 1

            slider += 1


        return low