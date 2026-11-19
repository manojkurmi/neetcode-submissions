class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        asked:
        - input are not sorted
        - sum to be zero
        - only uniq set
        - need to return value, not index
        sol:
        - sort input
        - run outer loop
            - run two pointer and check invariants
        - use set to maintain unique triplets
        """

        if not nums:
            return

        nums.sort()
        res = set()

        for i, num in enumerate(nums):
            left, right = i+1, len(nums)-1
            while left < right:
                sum_ = num + nums[left] + nums[right]
                if(sum_ < 0):
                    left += 1
                elif(sum_ > 0):
                    right -= 1
                else:
                    res.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return list(res)

        