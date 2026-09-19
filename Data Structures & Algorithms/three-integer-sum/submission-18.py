class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 1
        right = len(nums) - 1
        triplets = []
        nums.sort()

        for i in range(0, len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    prevLeft = nums[left]
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1

        return triplets
