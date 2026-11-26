class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0
        pos = 31
        while n:
            bit = n & 1
            n >>= 1
            reversed |= bit << pos
            pos -= 1
        return reversed
