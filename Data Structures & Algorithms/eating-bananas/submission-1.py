class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        given
        - piles of bananas
        - piles not sorted
        - h is hour to finish all bananas in
        asked
        - decide eating rate k
        - find k minimm
        constraint
        - cannot finish and start a pile in same hour
        - large number of piles and balanasa each pile
        edge:
        - hours less than piles: assured in problem
        return:
        - hour k
        sol:
        - sort the piles
        - binary searh the rate
        """

        piles.sort()
        left, right = 1, piles[-1]
        n = len(piles)
        min_k = piles[-1]

        while left <= right:
            mid = left + (right - left) // 2
            rate = mid
            # calculate hours taken
            hours = sum([(piles[i] + rate - 1) // rate for i in range(n)])
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
                min_k = min(min_k, rate)
            
        return min_k

