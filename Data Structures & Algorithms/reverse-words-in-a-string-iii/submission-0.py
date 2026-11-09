class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        chars = list(s)
        
        for right in range(1, len(chars)):
            if right == len(chars) - 1:
                # here is the end, we need to swap all char between left and right now
                self.swap_chars(chars, left, right)
            elif chars[right] == ' ':
                self.swap_chars(chars, left, right - 1)
                left = right + 1
                right = left + 1

        return "".join(chars)


    def swap_chars(self, chars, l, r):
        while l < r:
            temp_char = chars[l]
            chars[l] = chars[r]
            chars[r] = temp_char
            l += 1
            r -= 1
        
        

