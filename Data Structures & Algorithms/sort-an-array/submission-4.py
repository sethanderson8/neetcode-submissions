class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        self.mergeSort(nums, left, right)

        return nums


    def mergeSort(self, nums: List[int], left, right):
        # Base case - when left is greater or == than right, therefore only 1 or 0 elements
        # this is where we always stop and we just return to make it stop. We know at this
        # point, the 1 or 0 element array is sorted
        if left >= right:
            return

        # Divide and recurse. mid + 1 to account for
        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        # Merge
        left_half = nums[left : mid + 1]
        right_half = nums[mid + 1 : right + 1]

        placement_idx = left
        left_idx = 0
        right_idx = 0

        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                nums[placement_idx] = left_half[left_idx]
                left_idx += 1
            else:
                nums[placement_idx] = right_half[right_idx]
                right_idx += 1
            placement_idx += 1

        while left_idx < len(left_half):
            nums[placement_idx] = left_half[left_idx]
            left_idx += 1
            placement_idx += 1

        while right_idx < len(right_half):
            nums[placement_idx] = right_half[right_idx]
            right_idx += 1
            placement_idx += 1


        