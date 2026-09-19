class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeCheck = set()
        for num in nums:
            if num in dupeCheck:
                return True
            else:
                dupeCheck.add(num)

        return False
        