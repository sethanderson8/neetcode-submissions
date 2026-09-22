class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        longest_prefix = strs[0]

        for i in range(1, len(strs)):
            # if the cur prefix actually is not prefix of cur word
            # we are looking at, enter while loop that chops off last
            # char of common prefix until this statement holds true
            while not strs[i].startswith(longest_prefix):
                longest_prefix = longest_prefix[0 : len(longest_prefix) - 1]

        return longest_prefix

