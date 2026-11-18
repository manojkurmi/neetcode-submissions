# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]

        def helper(root, count):
            if not root or count >= k:
                return count
            count =  helper(root.left, count)
            count += 1
            if count == k:
                res[0] = root.val
                return count
            return helper(root.right, count)
        
        helper(root, 0)
        return res[0]
