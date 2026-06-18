class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            heap.append((self.calcDist(p[0],p[1]),p))
        
        heapq.heapify(heap)
        output = []

        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output

    def calcDist(self, x, y):
        dist2 = (pow(x,2) + pow(y,2))
        return pow(dist2, 0.5)   