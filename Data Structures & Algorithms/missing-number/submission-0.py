class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        n integeres
        no dups
        return single num that is missing in the range
        """
        xor = 0
        for i in range(len(nums)+1):
            xor ^= i

        for num in nums:
            xor ^= num
        
        return xor
    