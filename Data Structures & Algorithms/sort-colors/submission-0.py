class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # you know that the vals are only 0,1,2. So use a count array
        # then just set the indexes based on the count

        count = [0 for i in range(3)]
        for num in nums:
            count[num] += 1

        index = 0
        # this give 0,1,2
        for i in range(len(count)):
            # this give amount of times to repeat either 0,1,2
            for num in range(count[i]):
                nums[index] = i
                index += 1