import heapq
import typing

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap=[]
        for num in nums:
            self.pushing(num)

    def pushing(self, num: int):
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, num)

    def add(self, val: int) -> int:
        self.pushing(val)
        return self.min_heap[0]
        
