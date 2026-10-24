class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_dup = set()
        for num in nums:
            if num in check_dup:
                return True
            else:
                check_dup.add(num)

        return False