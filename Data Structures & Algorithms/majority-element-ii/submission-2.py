class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Use a hashmap, but always make sure the size of the hashmap is less
        # than 3
        # We will only have the top 2 most frequent elements here since, we can
        # at max return two numbers
        # When we hit over 3 in our hashmap, we -= 1 to each, any that reach 0 
        # were at 1 before the -=, we remove completely from the map
        # Special case, could reach the end and have 2 mins with count 1, we 
        # will need to iterate back over on these nums to check if their count
        # is actually greater than len(n) / 3
        # This hashmap will only have the 2 most common if they exist
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            if len(num_count) > 2:
                for num_key in list(num_count):
                    if num_count[num_key] == 1:
                        num_count.pop(num_key, None)
                    else:
                        num_count[num_key] = num_count.get(num_key, 0) - 1
        
        for num_key in num_count:
            num_count[num_key] = 0

        ans = []

        for num_key in num_count:
            if nums.count(num_key) > len(nums) / 3:
                ans.append(num_key)

        return ans


            


        