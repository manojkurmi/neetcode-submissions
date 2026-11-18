# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # edge case
        if not head or not head.next:
            return
        
        # find half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # terminate 1st list
        prev_slow = slow
        slow = slow.next
        prev_slow.next = None

        # reverse 2nd half
        reverse = None
        while slow:
            next_ = slow.next
            slow.next = reverse
            reverse = slow
            slow = next_
        
        # merge the list
        while reverse:
            h_next, r_next = head.next, reverse.next
            reverse.next = head.next
            head.next = reverse
            reverse = r_next
            head = h_next
        