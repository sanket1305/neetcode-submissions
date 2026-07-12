class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        heap = []

        for i in range(n):
            heapq.heappush(heap, (-nums[i], i))
            # print(i, heap)
            
            if i >= (k-1):
                # print("if")
                while (i - heap[0][1]) >= k:
                    heapq.heappop(heap)
                
                res.append(-heap[0][0])
        
        return res