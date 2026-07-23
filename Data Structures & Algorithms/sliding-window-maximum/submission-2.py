class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        heap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            if i >= k-1:
                while (i - heap[0][1]) >= k:
                    heapq.heappop(heap)
                
                res.append(-heap[0][0])
        
        return res