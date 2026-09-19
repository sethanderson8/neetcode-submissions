class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Left Sum
        # Right Sum

        # [1,2,4,6]

        # LeftSum: [0, 1, 2, 8]
        # RightSum: [48, 24, 6, 0]  NEED TO MAKE SURELEADING AND ENDING 0s are 1s for our math

        leftSum = [1] * len(nums)
        rightSum = [1] * len(nums)
        left = 0
        right = len(nums) - 1

        leftLastNum = 1
        rightLastNum = 1

        while left < len(nums) and right >= 0:
            rightSum[right] = rightLastNum
            rightLastNum *= nums[right]

            leftSum[left] = leftLastNum
            leftLastNum *= nums[left]
            left += 1
            right -= 1

        productExceptSelf = []

        for i in range(len(leftSum)):
            productExceptSelf.append(leftSum[i] * rightSum[i])

        return productExceptSelf

