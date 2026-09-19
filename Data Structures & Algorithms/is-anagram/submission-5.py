class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterCount = {}
        for char in s:
            letterCount[char] = letterCount.get(char, 0) + 1

        tLetterCount = {}
        for char in t:
            tLetterCount[char] = tLetterCount.get(char, 0) + 1

        for key in letterCount.keys():
            if letterCount.get(key) != tLetterCount.get(key, 0):
                return False

        return True
