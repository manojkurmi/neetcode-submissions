# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

NONE_NODE = "N"

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append(NONE_NODE)
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        idx = 0

        def dfs():
            nonlocal idx
            if idx >= len(vals):
                return None
            val = vals[idx]
            idx += 1
            if val == NONE_NODE:
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

    """
    given:
    - binary tree with val
    constraints:
    - 0 to 10K nodes
    - +/- values
    res:
    - tree to str to back tree
    edge:
    - empty
    - skewed tree
    sol:
    - do pre-order
    - store null if no child at that pos
    - can skip all trailing nulls
    runtime: n
    space: n
    helper:
    - dfs func
    """

