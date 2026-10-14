class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        max_len = 0
        left = right = 0

        while right < len(s):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            while (right - left + 1) - max(char_freq.values()) > k:
                char_freq[s[left]] = char_freq.get(s[left], 0) - 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
        