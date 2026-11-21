from heapq import heapify, heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ensure that duplicate key have proper comparotor
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node is not None]
        heapify(heap)
        head = tail = ListNode()

        while heap:
            val, idx, node = heappop(heap)
            tail.next = node
            tail = tail.next

            if(node.next):
                heappush(heap, (node.next.val, idx, node.next))

        return head.next
