class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        asked:
        - pick only two bar to get max water in that
        constraints:
        - min bar 2, max: 100K
        - height can be zero
        edge:
        - zero and either end
        sol:
        pattern: - two pointer
        steps: - find volume as you walk the pointere from both end
            - always look for higher height
        return:
        - int with max water, assuming middle bar doesn't exists

        """
        max_water = 0
        
        left, right = 0, len(heights)-1
        while left < right:
            curr_water = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, curr_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
