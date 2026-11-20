class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        given:
        - list of n+1 ints
        - range 1-n
        - only one repeated
        - input may not be sorted
        asked:
        - find repeated int
        constraint:
        - n upto 10K
        - followup: in O(1) extrace space, input as const
        sol:
        - will modify the input at idx-1 to negative
        - if negative means dup
        """

        # pivot at 28th minutes: solve use O(n) space, O(n) runttime
        def sol1(nums):
            seen = set()
            for val in nums:
                if val in seen:
                    return val
                seen.add(val)
            return 0
        
        return sol1(nums)
            
