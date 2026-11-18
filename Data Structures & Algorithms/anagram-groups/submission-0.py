from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[self.normalized(s)].append(s)
        
        return res.values()

    def normalized(self, s: str) -> str:
        return "".join(sorted(s))
    