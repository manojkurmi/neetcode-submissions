class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        given:
        - array of temps
        asked:
        - find warmer day in future
        constraints:
        - 100K temps
        - non zero temps
        sol:
        - iterate, and keep in list/stack non-incr temp.
        - on higher temp, pop and store the day diff result
        edgecase:
        - only one temp
        - no higher temp
        """

        st = [(float('inf'), -1)]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while temp > st[-1][0]:
                _, day = st.pop()
                res[day] = i - day
            st.append((temp, i))
        
        return res
