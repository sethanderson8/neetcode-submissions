class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to track when repeating letter happens
        # left and right pointer
        # iterate right pointer until it is equal to left pointer
        # iterate left pointer until ....
        left = 0
        right = 0
        maxSubstring = 0

        seenChars = set()

        while right < len(s):
            if s[right] in seenChars:
                while s[right] in seenChars:
                    seenChars.remove(s[left])
                    left += 1

            seenChars.add(s[right])
            maxSubstring = max(maxSubstring, right - left + 1)
            right += 1

        return maxSubstring