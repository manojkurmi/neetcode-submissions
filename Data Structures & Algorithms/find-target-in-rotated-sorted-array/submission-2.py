class Solution:
    def search(self, nums: List[int], target: int) -> int:
        le, ri = 0, len(nums)-1

        while le <= ri:
            mi = le + (ri-le) // 2
            if nums[mi] == target:
                return mi
            
            if nums[le] <= nums[mi]:
                if nums[le] <= target < nums[mi]:
                    ri = mi - 1
                else:
                    le = mi + 1
            else:
                if nums[mi] < target <= nums[ri]:
                    le = mi + 1
                else:
                    ri = mi - 1
        
        return -1

