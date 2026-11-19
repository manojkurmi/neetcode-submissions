# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = -1
        def dfs(root):
            nonlocal max_dia
            if not root:
                return -1
            left_dia = dfs(root.left)
            right_dia = dfs(root.right)
            # find max dia
            cur_dia = 0
            if root.left:
                cur_dia += 1 + left_dia
            if root.right:
                cur_dia += 1 + right_dia
            max_dia = max(max_dia, cur_dia)
            return 1 + max(left_dia, right_dia)
        
        dfs(root)
        return max_dia
