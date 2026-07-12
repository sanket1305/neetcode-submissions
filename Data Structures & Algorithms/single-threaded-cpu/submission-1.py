class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        res = []

        tasks = sorted([[x, y, idx] for idx, (x, y) in enumerate(tasks)])

        minHeap = []

        t = 0
        i = 0
        while len(res) < n:
            if not minHeap and t < tasks[i][0]:
                t = tasks[i][0]
            
            while i < n and tasks[i][0] <= t:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            prc_time, idx = heapq.heappop(minHeap)
            t += prc_time

            res.append(idx)
        
        return res