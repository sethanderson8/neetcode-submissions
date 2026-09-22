class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [a,b,c,d,e,f]
        # Output: [b*c*d*e*f,a*b*c*d*e*f/f,12,8]
        ans = [1] * (len(nums))
        prefix = 1
        # first go front to back
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        # Then go back to front
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans