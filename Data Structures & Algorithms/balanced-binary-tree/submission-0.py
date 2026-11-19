# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            left_bal, left_depth = dfs(root.left)
            # break early if left is unbalanced
            if not left_bal:
                return False, 1+left_depth
            
            right_bal, right_depth = dfs(root.right)

            is_balanced = right_bal and abs(left_depth-right_depth) <= 1
            return is_balanced, 1+max(left_depth, right_depth)

        bal, _ = dfs(root)
        return bal