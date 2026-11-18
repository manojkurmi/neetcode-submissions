from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter([ch for ch in s])
        ct = Counter([ch for ch in t])
        return cs == ct