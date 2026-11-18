class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in numMap:
                return [numMap[other], i]
            if num not in numMap:
                numMap[num] = i
        
        return None
