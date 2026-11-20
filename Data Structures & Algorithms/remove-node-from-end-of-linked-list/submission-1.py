# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        given:
        - head of the linked list
        - nth node to remove
        asked:
        - delete nth node fron end
        constraint:
        - 1 to 30 nodes
        - node val 0-100
        strategy:
        - slow/fast ptr
        sol:
        - find nth node
        - use slow/fast ptr, and delete at slow ptr
        edgecase:
        - head, tail, before head
        runtime: O(n)
        space: O(1)
        """

        if not head:
            return None

        dummy_head = ListNode(next=head)
        fast = dummy_head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1
        
        slow = dummy_head
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy_head.next
        

    """
    Brute:
    - 1st. move the values, and delete the last node
    - 2nd. count total node in 1st pass, and 2nd pass will delete element at that position.

    """
