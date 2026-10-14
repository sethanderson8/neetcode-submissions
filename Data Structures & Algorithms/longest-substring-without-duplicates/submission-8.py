class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = right = 0
        prev_idxs = {}

        while right < len(s):
            # if we have a duplicate that is actually in our window, then we skip ahead witth
            # the left. Inlusive for the window!!!
            if s[right] in prev_idxs and prev_idxs[s[right]] >= left:
                # Jump ahead with left
                left = prev_idxs[s[right]] + 1
            # Update the prev_idxs with cur char for s[right]
            prev_idxs[s[right]] = right
            # Update max_len if needed
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

        