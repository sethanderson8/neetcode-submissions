class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow_two = 0

        while slow != slow_two:
            slow = nums[slow]
            slow_two = nums[slow_two]

        return slow
        