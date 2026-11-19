class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        given:
        - string of char
        - empty to 50K chars
        - has printable chars
        sol:
        - sliding window and char set for uniqueness
        edge:
        - empty
        runtime: O(n)
        space: O(k)
        return: len of substring
        """

        left = 0
        n = len(s)
        state = set()
        max_len = 0

        for i, ch in enumerate(s):
            # if possible dup, keep on remove from left until dup is gone
            if ch in state:
                while s[left] != ch:
                    state.remove(s[left])
                    left += 1
                left += 1   # just advance , char is already in set
            else:
                state.add(ch)

            max_len = max(max_len, i-left+1)

        return max_len


            
            
