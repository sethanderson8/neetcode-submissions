class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_most = self.binary_search(nums, target, True)
        right_most = self.binary_search(nums, target, False)
        return [left_most, right_most]

        
    def binary_search(self, nums: list[int], target: int, left_search: bool):
        left = 0
        right = len(nums) - 1
        idx = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                idx = mid
                if left_search:
                    # lower bound search
                    right = mid - 1
                else:
                    # upper bound search
                    left = mid + 1
        return idx
