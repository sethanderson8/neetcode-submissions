class Solution:
    # THIS MEANS ENCODE TAKES A LIST OF STRING, CONVERTS TO ONE STRING
    # DECODE TAKES A SINGLE RETURN AND RETUNS A LIST OF STRINGS

    # One idea, use ?+length of string after+?
    # This woul dbe preceeding each string so..
    # ex. "Hello","World" -> "?5?Hello?5?World"
    # "" -> "?0?"
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += ('?' + str(len(word)) + ';' + word)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        char_counter = 0
        expected_word_length = 0
        cur_word = ""
        counting_word_len = False
        extracting_word = False

        for char in s:
            if not extracting_word:
                if char == ';':
                    counting_word_len = False
                    if expected_word_length == 0:
                        decoded_string.append("")
                    else:
                        extracting_word = True
                elif char == '?':
                    counting_word_len = True
                elif counting_word_len:
                    digit = ord(char) - ord('0')
                    expected_word_length = (expected_word_length * 10) + digit
            else:
                cur_word += char
                expected_word_length -= 1
                if expected_word_length == 0:
                    extracting_word = False
                    decoded_string.append(cur_word)
                    cur_word = ""

        return decoded_string

            
