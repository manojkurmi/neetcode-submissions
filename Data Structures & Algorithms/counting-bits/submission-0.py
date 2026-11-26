class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        - count num of 1's in binary of every nums in the range
        """
        res = []
        for num in range(0, n+1):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            res.append(count)
        
        return res