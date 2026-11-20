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
        save_dummy_head = Node(0, next=head)
        save_copy_head = copy_tail = Node(0)

        head = save_dummy_head
        while head.next:
            node = Node(head.next.val)
            node_map[head.next] = node

            copy_tail.next = node

            head = head.next
            copy_tail = copy_tail.next
        
        # restart
        head = save_dummy_head.next
        copy_head = save_copy_head.next
        while head:
            if head.random:
                copy_head.random = node_map[head.random]

            head = head.next
            copy_head = copy_head.next
        
        return save_copy_head.next





