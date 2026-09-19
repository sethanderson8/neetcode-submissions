class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Would want to find a left and right max
        # Start two pointers one on each end
        # track total max
        # return total max
        # Formula is min(left, right) * right - left

        left = 0
        right = len(heights) - 1
        maxWater = 0
        while left < right:
            currentWater = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, currentWater)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1

        return maxWater
        