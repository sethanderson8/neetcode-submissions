class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}

        for i in range(len(nums)):
            corresponding_num = target - nums[i]
            if corresponding_num in val_to_index:
                # You know that I will be the greater val if corresponding val
                # is in the map
                return [val_to_index[corresponding_num], i]
            else:
                val_to_index[nums[i]] = i

        return []

