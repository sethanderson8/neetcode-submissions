class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums_1_pointer = m - 1
        nums_2_pointer = n - 1
        last = m + n - 1

        while last >= 0:
            if nums_1_pointer >= 0 and nums_2_pointer >= 0 and nums1[nums_1_pointer] > nums2[nums_2_pointer]:
                nums1[last] = nums1[nums_1_pointer]
                nums_1_pointer -= 1
            elif nums_2_pointer >= 0:
                nums1[last] = nums2[nums_2_pointer]
                nums_2_pointer -= 1

            last -= 1


        