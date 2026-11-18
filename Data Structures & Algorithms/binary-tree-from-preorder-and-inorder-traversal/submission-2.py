# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we know the root is at beginning of preorder tree
        # indexs are inclusive
        # we can use hashmap to search for root in inorder tree
        in_map = {val: i for i, val in enumerate(inorder)}
        def helper(pre_b, pre_e, in_b, in_e):
            if pre_b > pre_e:
                return None
            root = TreeNode(val=preorder[pre_b])
            left_size = in_map.get(root.val) - in_b

            root.left = helper(pre_b+1, pre_b+left_size, in_b, in_b+left_size-1)
            root.right = helper(pre_b+left_size+1, pre_e, in_b+left_size+1, in_e)
            return root

        return helper(0, len(preorder)-1, 0, len(preorder)-1)
