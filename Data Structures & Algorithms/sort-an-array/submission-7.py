class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        self.merge_sort(nums, left, right)

        return nums

    def merge_sort(self, nums: list[int], left: int, right: int):
        # Base, Divide, Merge
        # Base
        if left >= right:
            # we return and stop recursing since we are at 0 or 1 char now
            return
        
        # Divide - recurse on left half and right half. Mid is the middle between left and right
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        # Merge - take the two halves based on left, mid, and right
        # then merge them together in the nums array
        # being careful to just overwrite the value we are currently sorting and merging together
        # left half, mid + 1 because non inclusive
        left_half = nums[left : mid + 1]
        # right half, mid + 1 inclusive, right + 1 since non inclusive
        right_half = nums[mid + 1 : right + 1]

        # pointer who right half, left half, and where to put sorted ints in nums
        # nums pointer starts at left since that is lowest idx of the slices we are sorting
        # so where we can overwrite the values in nums
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

        # There still could be values left in the left or right slices
        # Need to iterate over both of them and add any remaining
        # We will only end up doing it for one or neither since
        # the above while loop would not have exited if that was not the
        # case
        while left_idx < len(left_half):
            nums[nums_idx] = left_half[left_idx]
            nums_idx += 1
            left_idx += 1

        # Right half now
        while right_idx < len(right_half):
            nums[nums_idx] = right_half[right_idx]
            nums_idx += 1
            right_idx += 1
            

        


