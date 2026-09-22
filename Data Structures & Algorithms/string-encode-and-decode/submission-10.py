class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += str(len(strs[i])) + '?' + strs[i]

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        cur_index = 0
        cur_word_len = 0

        while cur_index < len(s):
            if s[cur_index].isdigit():
                cur_word_len = cur_word_len * 10 + int(s[cur_index])
            elif s[cur_index] == '?':
                decoded_string.append(s[cur_index + 1 : cur_index + 1 + cur_word_len])
                cur_index += cur_word_len
                cur_word_len = 0
            cur_index += 1

        return decoded_string
                
                