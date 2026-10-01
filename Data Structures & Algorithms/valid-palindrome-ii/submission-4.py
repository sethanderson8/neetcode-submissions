class Solution:
    def validPalindromeHelper(self, s: str, left: int, right: int):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # delete one letter on each and see if either are valid palindrome
                return (self.validPalindromeHelper(s, left + 1, right) or 
                        self.validPalindromeHelper(s, left, right - 1))
            left += 1
            right -= 1

        return True
