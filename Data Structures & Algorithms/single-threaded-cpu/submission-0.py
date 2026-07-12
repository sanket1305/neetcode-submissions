class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        res = []
        cnt = 0

        tasks = sorted([[x, y, idx] for idx, (x, y) in enumerate(tasks)])
        # print(tasks)
        # print()

        minHeap = []

        t = 0
        i = 0
        while len(res) < n:
            if i < n and t < tasks[i][0]:
                t += 1
                continue
            
            while i < n and tasks[i][0] <= t:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            # print(t, minHeap)
            prc_time, idx = heapq.heappop(minHeap)
            res.append(idx)
            t += prc_time

            cnt += 1
        
        return res