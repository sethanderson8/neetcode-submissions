class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force is essentially the triple loop solution
        # Two pointer here
            # Sort the array
            # for loop going from 0, nums(len) - 2, this is the left val
                # now do two pointers for mid and right
                    # mid = left + 1, right = len(nums) - 1
                        # Converge towards the middle using two sum sorted method

        nums.sort()
        ans = []
        for left in range(len(nums) - 2):
            # skip duplicates for the left!
            if left > 0 and nums[left] == nums[left - 1]:
                continue 
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                if nums[left] + nums[mid] + nums[right] < 0:
                    mid += 1
                elif nums[left] + nums[mid] + nums[right] > 0:
                    right -= 1
                else:
                    ans.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    # SKIP THE DUPLICATE VALS!
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
        return ans

        # We don't need a loop to skip 'right' duplicates. 
        # 'left' is fixed, and 'mid' is now strictly larger.
        # If 'right' is a duplicate, the new sum will be > 0, 
        # so the main loop will automatically decrement 'right' anyway.

        # test cases
        # array with duplicate vals
        # array with 3 vals and answer
        # array with 3 vals and no answer
        # array with all negatives
        # array with all positives
        # array with all the same val


        
