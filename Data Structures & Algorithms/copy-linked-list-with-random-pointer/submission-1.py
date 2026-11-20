"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        given:
        - list with node containg random pointer as well
        asked:
        - deep copy while maintaining structure
        constraint:
        - random to be maintained as corresponding to original
        - node value not unique
        sol:
        - traverse and create next and random if required
        - maintain hashmap of the node: orig to new
        runtime: O(n)
        space: O(n)
        edge: random nodes/null
        """
        # did reset in 20th minute

        node_map = {}
        def get_copy_node(node):
            if not node:
                return None
            if node not in node_map:
                node_map[node] = Node(node.val)
            return node_map[node]


        save_dummy_head = Node(0, next=head)
        save_copy_head = copy_tail = Node(0)

        head = save_dummy_head
        while head.next:
            copy_tail.next = get_copy_node(head.next)
            copy_tail.random = get_copy_node(head.random)

            head = head.next
            copy_tail = copy_tail.next

        # last node's ramdon ptr is not taken care of
        copy_tail.random = get_copy_node(head.random)
        
        return save_copy_head.next





