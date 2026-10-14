class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        highest_freq = max_len = 0
        left = right = 0

        while right < len(s):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            highest_freq = max(highest_freq, freqs[s[right]])

            num_chars_to_replace = (right - left + 1) - highest_freq
            # here we can just slide the window since we know any smaller window cannot
            # beat our current max_len
            if num_chars_to_replace > k:
                # decrement left in freqs
                freqs[s[left]] -= 1
                # move left
                left += 1
            
            # here, even if the window is invalid, we know that...
            max_len = right - left + 1
            right += 1

        return max_len