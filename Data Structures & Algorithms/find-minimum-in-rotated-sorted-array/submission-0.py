class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if array is sorted
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums)-1
        while left < right:
            if right-left == 1:
                return min(nums[left], nums[right])
            mid = left + (right-left)//2
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
        
        # will not reach this position
        return 0