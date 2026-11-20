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

        # pivot at 28th minutes: solve use O(n) space, O(n) runtime
        def sol1(nums):
            seen = set()
            for val in nums:
                if val in seen:
                    return val
                seen.add(val)
            return 0
        
        # return sol1(nums)

        # sol: modify in place O(1) space, O(nlogn) runtime
        def sol2(nums):
            nums.sort()
            for i in range(1, len(nums)):
                if nums[i-1] == nums[i]:
                    return nums[i]
            return 0
        
        # return sol2(nums)
        
        # sol: modify inplace O(1) spacem O(n) runtime, modified orig array
        def sol3(nums):
            for i in range(len(nums)):
                num = abs(nums[i])
                if nums[num-1] < 0:
                    return num
                nums[num-1] = -nums[num-1]
        
        # return sol3(nums)


        # binary search
        def sol4(nums):
            l, h = 1, len(nums) - 1
            while l < h:
                m = l + (h-l) // 2
                lessOrEqual = sum([1 for num in nums if num <= m])
                if lessOrEqual <= m:
                    l = m+1
                else:
                    h = m
            
            return l
        # return sol4(nums)

        # fast/slow
        def sol5(nums):
            slow, fast = 0, 0
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break
            
            slow2 = 0
            while True:
                slow = nums[slow]
                slow2 = nums[slow2]
                if slow == slow2:
                    return slow
        
        return sol5(nums)


