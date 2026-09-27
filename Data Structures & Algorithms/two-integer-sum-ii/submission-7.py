class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # + 1 to each found index, since we are using a 1 indexed answer instead of 0
        # Brute force
            # Iterating over each element in the array (First for loop)
                # Iterate over each element in the array at a greater index that the current (second for loop)
                    # if we find that the first num + second num == target, retun [index1 + 1, index2 + 1]

        # Predictable dynamic approach that is going to take advantage of this sorted array
        # Two pointer solution
            # One pointer at the start, One pointer that the end of the array
            # Since this is sorted, we know all value below the end pointer will be less than its cur val
                # We also know the opposite for the start pointer, where all values to the right, will be greater
                #  than its cur val
            # Any time you increment the start pointer, the summation of the two values (val at start pointer + val at end pointer)
                # will always be greater than or equal to the current summation
                # Same logic applies to end pointer, any time you move it left or decrement, we will always be less than or equal to
                # the current sumation
            # while left < right
                # if left val + right val < target
                    # left += 1
                # elif left val + right val > target
                    # right val -= 1
                # else (when we actually find the summation to the target val)
                    # return [left + 1, right + 1]
                        # + 1 because 1 indexed

            # return []

        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: # these are equal to the target here, return since the found the ans
                return [left + 1, right + 1]

        return []

        # Test Cases
            # empty array
            # array with two values that equal the target
                #[1,2], target = 3
            # array with two values that are not equal to the target
            # array with more than two vals equal to the target
            # array with more than two vals not equal to the target
            # array with duplicate vals
            # array with negative vals and positive vals that does return an answer
            # array with negative vals and positive vals where the target is also negative and returns an answer