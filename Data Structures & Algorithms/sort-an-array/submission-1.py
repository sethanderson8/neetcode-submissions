class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case so we dont split indefinitely
        if len(nums) <= 1:
            return nums

        # floor division for the length
        mid = len(nums) // 2

        # keep splitting up the array
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # actually merge the halves so they are sorted
        return self.merge(left, right)


    def merge(self, left, right) -> List[int]:
        sorted_array = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        
        # now append the leftovers
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array
        