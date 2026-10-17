class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # need to figure out which half is sorted for comparison to our target
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                # left half is sorted, check here if our target is in that sorted half
                if nums[left] <= target and nums[mid] > target:
                    # It is probs in our left half, search there
                    right = mid - 1
                else:
                    # Probs in our right half, search there
                    left = mid + 1
            else:
                if nums[right] >= target and nums[mid] < target:
                    # Probs in our right half, search there
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        # [4 ,5 ,6 ,7 ,0 ,1 ,2 ]
        #              l  r            