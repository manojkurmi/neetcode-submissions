# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        given:
        - two non empty lists
        - non negative ints
        - represents number iin reverse order
        asked:
        - sum of two list as number
        constraints:
        - 100 nodes/digits
        sol:
        - iterate from left and keep adding, keeping in mind carry
        - look for carry at the end
        runtime: O(n)
        space: O(n)
        """

        carry = 0
        head = tail = ListNode()

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            carry = val // 10
            val = val % 10
            tail.next = ListNode(val)
            tail = tail.next

        return head.next


        """
        Brute:
        - get number from the list, then add
        """