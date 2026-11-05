class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        self.prefix_sum = prefix_sum

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# [-2,0,3,-5,2,-1]
# -2,-2,1,-4,-2,-3
# Formula is get the prefix sum from the right and subtract the prefix sum of left - 1, if in bounds