class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        return self.searchRecurse(nums, target, start, end)



    def searchRecurse(self, nums: List[int], target: int, start, end) -> int:
        mid = (start + end) // 2
        if start > end:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.searchRecurse(nums, target, mid + 1, end)
        elif nums[mid] > target:
            return self.searchRecurse(nums, target, start, mid - 1)
            
