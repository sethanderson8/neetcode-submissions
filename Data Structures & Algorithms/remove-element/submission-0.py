class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length_of_initial_array = len(nums)
        earliest_val_index = 0  # Tracks where to overwrite (the write pointer)

        # next_good_num_index acts as our read pointer scanning every item
        for next_good_num_index in range(length_of_initial_array):
            if nums[next_good_num_index] != val:
                nums[earliest_val_index] = nums[next_good_num_index]
                earliest_val_index += 1
                
        # earliest_val_index naturally represents the count of valid elements
        return earliest_val_index

                    
