class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        # Best area var that will get updated
        # wider is better so pointers will be opposite ends of height
        # while left < right
        # Do max area calc
            # current area min(heights[left], heights[right])
                # * (right - left)
            # max area = max(max area, cur area)
            # idea is move whichever is smaller in terms of height bc
            # the only way you can beat the cur max area is if it gets taller bc rn it is 
            # getting skinnier
            # If tied, just pick one and while again
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            cur_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, cur_area)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1

        return max_area

        #test cases
        # just two heights
        # complete 0 array
        # height of 1 tall, one 0
        # array of all same heights

