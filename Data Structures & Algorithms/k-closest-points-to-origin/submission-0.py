from heapq import heapify, heappop
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        given:
        - list of co-ordinates
        - to find k closest poitns to the origin (0,0)
        constraints:
        - 1 to 1000 co-ords
        - points are pos and neg
        sol:
        - calc dist and create heap
        - get top k from heap
        complexity:
        runtime: k*logn
        space: n
        edge:
        - no point, no k
        """

        if len(points) <= k:
            return points

        heap = [(sqrt(x*x + y*y), (x,y)) for (x, y) in points]
        heapify(heap)

        res = []
        for i in range(k):
            _, point = heappop(heap)
            res.append(point)

        return res
