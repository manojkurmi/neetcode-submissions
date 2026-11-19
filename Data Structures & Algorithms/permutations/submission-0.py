class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        given:
        - list of numbers
        - max 6 numbers
        return:
        list of all permutations
        sol:
        - fix a number (at position), and create all permutation for others, => add to sol => then backtrack
        edge: empty set
        """

        if not nums:
            return []
        sets = [[nums[0]]]

        for num in nums[1:]:
            new_sets = []
            for perm in sets:
                for i in range(len(perm)+1):
                    new_sets.append(perm[:i] + [num] + perm[i:])
            sets = new_sets

        return sets

