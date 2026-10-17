class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                # we are in the left sorted sorted portion
                if nums[mid] < target or nums[left] > target:
                    # search right if the cur number is less than target or the left num
                    # is greater than the target
                    left = mid + 1
                else:
                    # search the left
                    right = mid - 1
            else:
                # we are in the right sorted portion of array. Our left value is greater than
                # the mid value we are looking at [6,1,2]
                if nums[mid] > target or nums[right] < target:
                    # search left
                    right = mid - 1
                else:
                    # search the right
                    left = mid + 1

        return -1

