from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        given:
        - list of stone weight
        - pick two heaviest stone, and keep the diff as net weight
        res:
        - last remaining stone weight
        sol:
        - use heap to pick two heaviest
        - store the net stone again to heap
        - last stone is the ans
        complexity:
        runtime: nlogn
        space: nlogn
        constraint:
        - 1 to 20 stones
        - non zero weights
        edge:
        - 1 stone
        side effect:
        - modifies the input list
        """

        heap = [-val for val in stones]
        heapify(heap)

        while len(heap) > 1:
            one, two = -heappop(heap), -heappop(heap)
            new_stone = abs(one-two)
            heappush(heap, -new_stone)
        
        return -heap[0]
