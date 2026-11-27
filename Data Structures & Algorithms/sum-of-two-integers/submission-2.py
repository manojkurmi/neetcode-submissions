class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            res |= (a_bit ^ b_bit ^ carry) << i
            carry = (a_bit & b_bit) | ((a_bit | b_bit) & carry)
        
        if res > 0x7FFFFFFF:
            return ~(res ^ 0xFFFFFFFF)
        return res