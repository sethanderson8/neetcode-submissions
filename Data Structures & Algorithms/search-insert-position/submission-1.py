class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # search the right half
                left = mid + 1
            else:
                # search the left half
                right = mid - 1

        # left == right here, no match
        if nums[left] >= target:
            # Target index here should be the cur index
            return left
        else:
            # Target index is greater than our cur index or should be to the right of it
            return left + 1
