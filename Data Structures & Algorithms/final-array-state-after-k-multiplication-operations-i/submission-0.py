class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = []
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        
        while k:
            val, idx = heapq.heappop(heap)
            heapq.heappush(heap, (val * multiplier, idx))
            k -= 1

        heap.sort(key = lambda x: x[1])

        for val, idx in heap:
            res.append(val)
        
        return res