class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        - sum of two ints without using +/- ops
        - bit and and continuous carry
        """

        res = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = (a_bit ^ b_bit ^ carry)
            res |= cur_bit << i

            carry = (a_bit & b_bit) | ((a_bit | b_bit) & carry)
        
        if res > 0x7FFFFFFF:
            return ~(res ^ 0xFFFFFFFF)

        return res
    
            