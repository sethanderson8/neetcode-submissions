class Solution:
    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n > 0:
            singleDigit = n % 10
            n = n // 10
            res += (singleDigit * singleDigit)
        return res

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)

        if slow == 1:
            return True
        else:
            return False

        