class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs.sort()

        longest_prefix = ""
        
        first_word = strs[0]
        last_word = strs[-1]

        cur_char_index = 0
        while cur_char_index < len(first_word) and first_word[cur_char_index] == last_word[cur_char_index]:
            longest_prefix += first_word[cur_char_index]
            cur_char_index += 1

        return longest_prefix

        
