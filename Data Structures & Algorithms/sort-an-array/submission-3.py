class Solution:
    def merge(self, nums: List[int], left, middle, right):
        # Here is where you actually do need to use mem, to split up the array into
        # its respective partition then sort it. Take note of the + 1 when on the non
        # inclusive value
        leftHalf = nums[left: middle + 1]
        rightHalf = nums[middle + 1: right + 1]

        # Now you have 3 pointers, one for leftHalf idx, one for rightHalf idx
        # last one on where to put sorted elements in the array
        leftIdx = 0
        rightIdx = 0
        # you use left since that is the first element of the portion we are sorting in the array
        arrayIdx = left

        while leftIdx < len(leftHalf) and rightIdx < len(rightHalf):
            if leftHalf[leftIdx] < rightHalf[rightIdx]:
                nums[arrayIdx] = leftHalf[leftIdx]
                leftIdx += 1
            else:
                nums[arrayIdx] = rightHalf[rightIdx]
                rightIdx += 1
            arrayIdx += 1

        # Now we have to add the leftovers. But we cannot do the slicing trick since we are doing
        # this in place. Also only one of these while loops will run
        while leftIdx < len(leftHalf):
            nums[arrayIdx] = leftHalf[leftIdx]
            leftIdx += 1
            arrayIdx += 1

        while rightIdx < len(rightHalf):
            nums[arrayIdx] = rightHalf[rightIdx]
            rightIdx += 1
            arrayIdx += 1

    def mergeSort(self, nums: List[int], left, right):
        if left >= right:
            # once no more to split, just return
            return 

        # mid point
        mid = (left + right) // 2

        # divide
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        # merge
        self.merge(nums, left, mid, right)




    def sortArray(self, nums: List[int]) -> List[int]:
        # base case
        # divide
        # merge
        left = 0
        right = len(nums) - 1
        # since we are doing in place and this does not return, we have to return nums after
        self.mergeSort(nums, left, right)
        return nums

        