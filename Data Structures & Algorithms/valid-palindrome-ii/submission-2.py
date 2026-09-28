class Solution:
    def validPalindromeHelper(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        deleted_char = False

        while left < right:
            if s[left] != s[right]:
                # dont slice here since that will create extra memory
                return self.validPalindromeHelper(s, left + 1, right) or self.validPalindromeHelper(s, left, right - 1)
            left += 1
            right -= 1

        return True

