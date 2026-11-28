class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        for _ in range(1, n):
            one, two = two, one+two
        return one