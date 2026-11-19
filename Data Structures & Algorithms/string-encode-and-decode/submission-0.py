class Solution:

    """
    [len][$][bytes][len][$][bytes]...
    """
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}$")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < len(s):
            start = i
            # get length
            while i < n and s[i] != "$":
                i += 1
            word_len = int(s[start:i])
            i += 1
            res.append(s[i : i+word_len])
            i += word_len
        
        return res
        

