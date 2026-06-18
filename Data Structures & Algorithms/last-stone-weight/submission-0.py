class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            a,b = heapq.heappop_max(heap), heapq.heappop_max(heap)
            if a == b:
                continue
            else:
                a = a - b
                heapq.heappush_max(heap, a)

        if len(heap) > 0:
            return heap[0]
        return 0 