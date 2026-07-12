class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        res = []

        while heap:
            print(heap)
            cnt, char = heapq.heappop(heap)
            if cnt == 0:
                continue

            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    return ''.join(res)

                extra_cnt, extra_char = heapq.heappop(heap)

                res.append(extra_char)
                if extra_cnt < -1:
                    heapq.heappush(heap, (extra_cnt + 1, extra_char))
                heapq.heappush(heap, (cnt, char))
            else:
                res.append(char)
                
                if cnt < -1:
                    heapq.heappush(heap, (cnt + 1, char))
        
        return ''.join(res)