class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = [ch for ch in s]
        ta = [ch for ch in t]
        sa.sort()
        ta.sort()

        return sa == ta