class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        given: prices
        sol:
        - find a pair with lowest price, followed by highest price
        constraints:
        - prices can be zero
        - only one price possible
        edge:
        - only 1 price
        approach: single pointer, with running min 
        """

        if(len(prices)) < 2:
            return 0

        running_min = float('inf')
        max_profit = 0

        for val in prices:
            if val < running_min:
                running_min = val
            else:
                max_profit = max(max_profit, val - running_min)
        
        return max_profit
