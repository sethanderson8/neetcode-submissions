class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        uniquePermutations = []
        usedIndexes = [False] * len(nums)
        self.backtrackPermute(nums, [], uniquePermutations, usedIndexes)

        return uniquePermutations

    def backtrackPermute(self, nums, currentPermutation, uniquePermutations, usedIndexes):
        if len(currentPermutation) == len(nums):
            uniquePermutations.append(currentPermutation[:])
        else:
            for i in range(len(nums)):
                if not usedIndexes[i]:
                    currentPermutation.append(nums[i])
                    usedIndexes[i] = True
                    self.backtrackPermute(nums, currentPermutation, uniquePermutations, usedIndexes)
                    currentPermutation.pop()
                    usedIndexes[i] = False