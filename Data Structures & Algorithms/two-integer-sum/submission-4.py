class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        corresponding_val_to_index = {}
        for i in range(len(nums)):
            if (target - nums[i]) in corresponding_val_to_index:
                return [corresponding_val_to_index[target - nums[i]], i]
            else:
                corresponding_val_to_index[nums[i]] = i

        return []