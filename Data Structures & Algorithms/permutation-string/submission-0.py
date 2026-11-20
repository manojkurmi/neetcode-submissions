class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        given:
        - string and pattern to find
        - match any order/form of pattern
        return:
        - true/false
        pattern:
        - sliding window
        sol:
        - make a freq of pattern
        - in sliding window, maintain the freq of window. match if freq are equal in structure
        edge cases:
        - pattern longer than input
        - input empty, pattern empty
        """

        pat = s1
        s = s2
        pat_freq = Counter(pat)
        state = defaultdict(int)

        def check_equal():            
            if(len(state) == len(pat_freq)):
                for key in state.keys():
                    if pat_freq[key] == None or state[key] != pat_freq[key]:
                        return False
                return True
            return False

        if len(s) < len(pat):
            return False

        left, right = 0, len(pat)-1

        for i in range(len(pat)):
            state[s[i]] += 1
        
        if(check_equal()):
            return True

        while (right+1) < len(s):
            right += 1
            state[s[right]] += 1

            state[s[left]] -= 1
            if(state[s[left]] == 0):
                del state[s[left]]
            left += 1

            if(check_equal()):
                return True
            
        return False
            



