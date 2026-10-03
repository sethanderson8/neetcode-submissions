class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # can be any num, point is that it has no votes. Should be the first ele actually in case of single ele array
        cur_max_element = nums[0]
        # votes initially start at 0
        cur_max_element_vote = 1

        for i in range(1, len(nums)):
            # voted out, switch to current element as max when votes get to 0
            if cur_max_element_vote == 0:
                cur_max_element = nums[i]

            if nums[i] == cur_max_element:
                # each new vote for the cur max ele, they get += 1
                cur_max_element_vote += 1
            else:
                # all diff votes for not the cur max ele, is -= 1 since they are different
                cur_max_element_vote -= 1
        return cur_max_element
        