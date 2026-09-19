class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            # since it sorted, we skip for duplicates in a row
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return triplets
