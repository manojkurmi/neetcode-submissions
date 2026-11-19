from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)

        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if not self.heap or len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappush(self.heap, val)
            heappop(self.heap)

        res = self.heap[0]
        return res


        """
        given:
        - k and initial nums
        - stream of int
        - find kths largest on add
        constraints:
        - k is 1 to 1000
        - initial list upto 1000
        - val can be negative
        - always at least k ints in strem for kth operation
        pattern: heap
        sol:
        - add initial nums to heap
        - on add, add and get kth largest
        edge:
        - 
        runtime: log k
        space: k
        """

        """
        Brute:
        - sort the input array
        - on add, insert element at position
        - return kth position item from the list
        """