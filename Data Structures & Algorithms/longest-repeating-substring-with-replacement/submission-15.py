class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = right = 0

        # map of chars to freq
        char_freqs = {}

        # tracking the highest char freq we have seen in a valid sliding window
        max_char_freq_within_window = 0

        # Idea here the result can only increase if we find a new larger max char frequency
        # within our current window
        while right < len(s):
            # we gotta update its freq in the map
            char_freqs[s[right]] = char_freqs.get(s[right], 0) + 1
            # then update of historical max char freq within a legal window
            max_char_freq_within_window = max(max_char_freq_within_window, char_freqs[s[right]])
            # max_char_freq_within_window + k = The absolute max legal len the window can ever be.
            # (right - left + 1) = the current length of the window
            
            # If current length of the window > max legal len:
            # Our window just got too big. We don't care what letters are inside it.
            # It mathematically exceeded our historical limit, so we pull 'left' 
            # forward to chop it back down to the legal size.
            
            # the only way a prev char freq can be beat here is if we have a new max_char_freq_within_window
            # in the current window. Then we would not enter this and the window would expand
            while (right - left + 1) - max_char_freq_within_window > k:
                # we will shrink the left window
                # First decrement its count in char_freqs
                char_freqs[s[left]] = char_freqs.get(s[left], 0) - 1
                # Keep shrinking the window
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len









