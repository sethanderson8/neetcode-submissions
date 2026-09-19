class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Go through list
        # sort the word and add the sorted word and word to the map
        # If present, simply add word to the value of that sorted word key
        # return values() as list

        anagrams = {}

        for string in strs:
            sortedWord = "".join(sorted(string))
            print(sortedWord)
            if not sortedWord in anagrams:
                anagrams[sortedWord] = [string]
            else:
                anagrams[sortedWord].append(string)

        return list(anagrams.values())
        