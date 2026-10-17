class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # if there are less total candies than kids, then it is 0
        # need to maximize candies given to each kid
        # candies to one kid cannot come from multiple piles
        # Binary search to try various amounts of candies to see what is valid and what
        # the max valid amount of candy we can give per kid
        # start at 1 since that is the min, 0 will be our default if nothing is found that
        # is valid. Max would be one kid, so the max size of one of the candy piles
        # each pile we do floor division based on the cur_candy_size_per_kid we are looking at
        # If not valid, we need to look at a smaller candy size. if valid we need to look at a larger
        # candy pile. Validity is determine by a kids_fed_counter which is incremented by each
        # candy pile looked at by doing integer division. Once the kids_fed_counter >= k, we know it is valid
        # and will see if there is a larger amount of candy we can give per kid
        candy_size_per_kid = 0
        left = 1
        # right = max(candies), optimization is to do sum(candies) // k
        # since we know that absolute max a kid can receive is the total sum of candies over k, (all even piles)
        right = sum(candies) // k
        
        while left <= right:
            mid = left + (right - left) // 2
            is_valid_mid = self.is_valid_candy_size_per_kid(candies, mid, k)
            if is_valid_mid:
                # The mid we just chose is valid so update our candy_size_per_kid and look for a bigger amount 
                # that is also valid
                candy_size_per_kid = mid
                left = mid + 1
            else:
                # The mid we chose was too big and cannot feed all the kids, so look for a smaller amount
                # that is valid
                right = mid - 1

        return candy_size_per_kid

    def is_valid_candy_size_per_kid(self, candies: list[int], candy_size_per_kid: int, k: int) -> bool:
        kids_fed = 0
        for candy_pile in candies:
            kids_fed += candy_pile // candy_size_per_kid
            if kids_fed >= k:
                return True
        return False

