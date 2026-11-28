class Solution:
    def rob(self, nums: List[int]) -> int:
        # res = [0, 0]
        # for i in range(len(nums)):
        #     res.append(max(res[-2] + nums[i], res[-1]))
        
        # return res[-1]

        prev, cur = 0, 0
        for i in range(len(nums)):
            prev, cur = cur, max(prev + nums[i], cur)
        
        return cur