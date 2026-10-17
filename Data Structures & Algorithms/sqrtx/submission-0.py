class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        lowest_sqrt = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                lowest_sqrt = mid
            else:
                return mid

        return lowest_sqrt
