class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify_max(self.maxheap)


    def addNum(self, num: int) -> None:
        if self.minheap and num > self.maxheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush_max(self.maxheap, num)
        
        one, two = len(self.minheap), len(self.maxheap)

        if abs(one-two) > 1:
            if one > two:
                val = heapq.heappop(self.minheap)
                heapq.heappush_max(self.maxheap, val)
            else:
                val = heapq.heappop_max(self.maxheap)
                heapq.heappush(self.minheap, val)
    

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + self.maxheap[0])/2
        else:
            one, two = len(self.minheap), len(self.maxheap)
            if one > two:
                return self.minheap[0]
            else:
                return self.maxheap[0]