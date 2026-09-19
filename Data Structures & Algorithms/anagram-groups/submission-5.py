class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict of key to List
        # Then go over each string
            # Create a tuple of 26 0s to count the number of letters
            # in that string
            # then go over each char is that string to fill out the 
            # tuple char count of each letters
        #Once out of inner for loop, check if said tuple is already in  the dict
        # of key to list. regardless, you will append to the list that is there for
        # that tuple since it is an empty list

        tuple_key_to_list = defaultdict(list)

        for str in strs:
            key_array = [0] * 26
            for char in str:
                key_array[ord(char) - ord('a')] += 1
            tuple_key_to_list[tuple(key_array)].append(str)

        return list(tuple_key_to_list.values())
