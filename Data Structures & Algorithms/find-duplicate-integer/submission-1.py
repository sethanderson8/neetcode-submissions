class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # there is some trick here since it is n+1 ints in a len n list and also the range is 1,n inclusive
        # negative marking
        # each num corresponds to an index, specifically val - 1
        # each time we visit a num, we mark it as negative. Iterate over all nums for loop
        # if we do end up seeing a negative again, the first would be the duplicate
        # so we would return abs(val)
        
        for i in range(len(nums)):
            # need to do abs here since it could be negative already
            idx = abs(nums[i]) - 1
            # actual check if that index is already negative, that is the duplicate since it has been visited already
            if nums[idx] < 0:
                return abs(nums[i])
            # Now mark the num at idx as negative
            nums[idx] *= -1


        return -1


