class Solution:
    def encode(self, strs: List[str]) -> str:
        # do num and ? at beginning of word
        encodedWord = ""
        for i in range(len(strs)):
            encodedWord += str(len(strs[i])) + "?" + strs[i]
        print(encodedWord)
        return encodedWord

    def decode(self, s: str) -> List[str]:
        decodedList = []
        currentLength = 0
        curIndex = 0
        while curIndex < len(s):
            if s[curIndex].isdigit():
                currentLength = currentLength * 10 + int(s[curIndex])
            elif s[curIndex] == "?":
                decodedList.append(s[curIndex + 1: curIndex + currentLength + 1])
                curIndex += currentLength
                currentLength = 0
            curIndex += 1

        return decodedList