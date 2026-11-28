class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        two pass:
            - 1. start with 1st house
            - 2. start with 2nd house
        take max of above
        """

        def helper(s, e):
            prev, cur = 0, 0
            for i in range(s, e):
                prev, cur = cur, max(cur, prev + nums[i])
            return cur
        
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(helper(0, n-1), helper(1, n))