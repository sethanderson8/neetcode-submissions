class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Need itt to be sorted first
        nums.sort()
        ans = []
        
        # Iterate from 0 to end of nums - 3
        for i in range(len(nums) - 3):
            # Skip duplicate for i elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Iterate from i+1 to end of nums - 2
            for j in range(i + 1, len(nums) - 2):
                # Skip duplicate for j elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur_sum < target:
                        # Search for larger num
                        left += 1
                    elif cur_sum > target:
                        # Search for smaller num
                        right -= 1
                    else:
                        # cur_sum == target, now append
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        # Move both pointers
                        left += 1
                        right -= 1
                        # Skip duplicate left elements
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicate right elements
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return ans

                    
