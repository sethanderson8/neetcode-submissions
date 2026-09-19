class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            if target - nums[i] in compliments.keys():
                return [compliments.get(target - nums[i]), i]
            compliments[nums[i]] = i

        return []