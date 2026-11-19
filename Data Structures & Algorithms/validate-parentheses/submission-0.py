class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
                     ']': '[',
                     '}': '{',
                     ')': '(',
                     }
        
        st = []
        for ch in s:
            if ch in paren_map.values():
                st.append(ch)
            elif st and st[-1] == paren_map.get(ch):
                st.pop()
            else:
                return False
        
        return len(st) == 0
