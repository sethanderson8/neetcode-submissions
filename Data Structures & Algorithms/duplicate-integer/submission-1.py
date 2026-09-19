class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupChecker = set()

        for num in nums:
            if num in dupChecker:
                return True
            else:
                dupChecker.add(num)

        return False
         