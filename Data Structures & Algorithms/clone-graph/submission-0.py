"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        deep clone graph with all note
        node 1 - n
        n total number of nodes
        1st node as input

        maintain hashmap
        1. : clone the nodes, store in hashmap
        2. traverse nodes and do the same
        3. maintain the nodes which need cloning as stack
        repeat above two steps

        
        """
        clone = []
        cache = {}
        processed = set()
        
        def getNode(nd):
            if not nd:
                return None
            if nd not in cache:
                cache[nd] = Node(nd.val)
            return cache[nd]
        
        stack = [node]
        cloned_root = None

        while stack:
            curr_node = stack.pop()
            if not curr_node or curr_node in processed:
                continue

            cloned = getNode(curr_node)

            if not cloned_root:
                cloned_root = cloned

            for nd in curr_node.neighbors:
                cloned.neighbors.append(getNode(nd))
                stack.append(nd)

            processed.add(curr_node)
        
        return cloned_root

            


