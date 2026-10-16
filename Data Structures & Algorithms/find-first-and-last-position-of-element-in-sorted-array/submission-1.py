class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        left_most = -1
        right_most = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # found the target, so we at least have a left and right most at min
                left_most = right_most = mid
                break
            elif nums[mid] < target:
                # search right half
                left = mid + 1
            else:
                # search left half
                right = mid - 1

        # the entire array could be nums so even if target is found need to explore both left
        # even when target is found

        # if we have at least found one num of the target
        if left_most >= 0:
            # search both left half and right half
            left_1 = left
            right_1 = right
            while left_1 <= right_1:
                mid = left_1 + (right_1 - left_1) // 2
                if nums[mid] == target:
                    left_most = mid
                    # search left half for a lower index of that target num
                    right_1 = mid - 1
                else:
                    # we know the num is too small since this is the left half
                    # need to search right half until equal again
                    left_1 = mid + 1
                    
            left_2 = left
            right_2 = right
            while left_2 <= right_2:
                mid = left_2 + (right_2 - left_2) // 2
                if nums[mid] == target:
                    right_most = mid
                    # search right half for a higher index of that target num
                    left_2 = mid + 1
                else:
                    # we know the num is too big since this is the right half
                    # need to search left half until equal again
                    right_2 = mid - 1
            
        return [left_most, right_most]
