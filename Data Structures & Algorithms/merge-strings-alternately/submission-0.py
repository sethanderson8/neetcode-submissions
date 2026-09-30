class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_ind = 0
        word2_ind = 0

        ans = []

        while word1_ind < len(word1) and word2_ind < len(word2):
            ans.append(word1[word1_ind])
            word1_ind += 1

            ans.append(word2[word2_ind])
            word2_ind += 1

        # Append whatever is left of both strings (one of these will just be an empty string)
        # It is fine in python tot do this because slicing out of bounds for the inclusive value will
        # still return "" and not error out
        ans.append(word1[word1_ind:])
        ans.append(word2[word2_ind:])
        
        return "".join(ans)