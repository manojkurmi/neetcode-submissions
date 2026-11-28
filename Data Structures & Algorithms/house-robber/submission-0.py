class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0, 0]
        for i in range(len(nums)):
            res.append(max(res[-2] + nums[i], res[-1]))
        
        return res[-1]
