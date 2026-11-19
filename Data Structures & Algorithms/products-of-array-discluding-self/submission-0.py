class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        # from left
        prod = 1
        for i in range(n):
            res[i] = prod
            prod *= nums[i]

        # from right
        prod = 1
        for i in range(n-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        
        return res
