class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        # now the fast and slow pointer are at the intersection, not the start of the cycle though
        # we need to find the second point of intersection by moving a slow pointer
        # from the start and the start of the first intersection
        # once they meet up and have the same val, that will be the start of the cycle
        slow_from_start = 0

        while slow_from_start != slow:
            slow = nums[slow]
            slow_from_start = nums[slow_from_start]

        return slow_from_start