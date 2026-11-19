# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # record the max sum with global state, and return max sum passing through this node

        max_sum = float('-inf')

        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            max_sum = max(max_sum, root.val + max(0, left_sum, right_sum, left_sum+right_sum))
            return root.val + max(0, left_sum, right_sum)
        
        dfs(root)
        return max_sum
