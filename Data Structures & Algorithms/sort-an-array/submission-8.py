class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        self.sort_helper(nums, left, right)

        return nums

    def sort_helper(self, nums: list[int], left: int, right: int):
        # Base
        if left >= right:
            return
        
        # divide
        mid = left + (right - left) // 2
        self.sort_helper(nums, left, mid)
        self.sort_helper(nums, mid + 1, right)

        # merge
        left_half = nums[left : mid + 1]
        right_half = nums[mid + 1 : right + 1]
        left_idx = right_idx = 0
        nums_idx = left

        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                nums[nums_idx] = left_half[left_idx]
                left_idx += 1
            else:
                nums[nums_idx] = right_half[right_idx]
                right_idx += 1
            nums_idx += 1

        while left_idx < len(left_half):
            nums[nums_idx] = left_half[left_idx]
            left_idx += 1
            nums_idx += 1

        while right_idx < len(right_half):
            nums[nums_idx] = right_half[right_idx]
            right_idx += 1
            nums_idx += 1
