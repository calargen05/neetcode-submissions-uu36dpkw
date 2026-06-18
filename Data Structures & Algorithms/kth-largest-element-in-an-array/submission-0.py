class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        for i in range(k):
            if i == k-1:
                return heapq.heappop_max(heap)
            else:
                heapq.heappop_max(heap)