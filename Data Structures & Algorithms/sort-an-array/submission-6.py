class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        self.merge_sort(nums, left, right)
        return nums

    def merge_sort(self, nums: list[int], left: int, right: int):
        if left >= right:
            return
        
        mid = (right + left) // 2

        self.merge_sort(nums, mid + 1, right)
        self.merge_sort(nums, left, mid)

        left_half = nums[left : mid + 1]
        right_half = nums[mid + 1 : right + 1]

        l = r = 0
        ans_idx = left

        while l < len(left_half) and r < len(right_half):
            if left_half[l] < right_half[r]:
                nums[ans_idx] = left_half[l]
                l += 1
            else:
                nums[ans_idx] = right_half[r]
                r += 1
            ans_idx += 1

        while l < len(left_half):
            nums[ans_idx] = left_half[l]
            l += 1
            ans_idx += 1

        while r < len(right_half):
            nums[ans_idx] = right_half[r]
            r += 1
            ans_idx += 1