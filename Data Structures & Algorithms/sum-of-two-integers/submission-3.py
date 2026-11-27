class Solution:
    def getSum(self, a: int, b: int) -> int:
        def sol1():
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

        def sol2(a, b):
            mask =    0xFFFFFFFF
            max_int = 0x7FFFFFFF

            while b != 0:
                carry = (a & b) << 1
                a = (a ^ b) & mask
                b = carry
            
            return a if a <= max_int else ~(a ^ mask)

        return sol2(a, b)

 
