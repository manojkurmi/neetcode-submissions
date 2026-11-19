class Solution:
    def trap(self, height: List[int]) -> int:
        """
        given:
        - list of bar heights, non-negative
        - each bar is 1 unit wide
        constraints:
        - 1 to 20K bars
        - 0 to 100K height
        asked:
        - find water trapped
        - to exclude bar volume
        approach:
            - two pointer
        sol:
            - traverse from left
            - for each bar, record water if it is smaller than left and right bar
            - keep record of highest bar so far on left
        complexity:
            runtime: O(n)
            space: O(1)
        edge case: only one bar, or two bar
        return:
            total water trapped
        """

        water_trapped = 0
        if(len(height)) <= 2:
            return 0
        
        left_max_h, right_max_h = height[0], height[-1]
        left, right = 1, len(height)-2

        while left <= right:
            if height[left] > left_max_h:
                left_max_h = height[left]
                left += 1
            elif height[right] > right_max_h:
                right_max_h = height[right]
                right -= 1
            else:
                if(left_max_h < right_max_h):
                    water_trapped += min(left_max_h, right_max_h) - height[left]
                    left += 1
                else:
                    water_trapped += min(left_max_h, right_max_h) - height[right]
                    right -= 1
        
        return water_trapped
