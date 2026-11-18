# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        state = [float('-inf')]

        def helper(root):
            if not root:
                return 0

            count = 0
            if root.val >= state[-1]:
                count += 1
            state.append(max(root.val, state[-1]))
            count += helper(root.left)
            count += helper(root.right)
            state.pop()
            return count
        
        return helper(root)
