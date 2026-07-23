class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        res = []
        l = 0
        q = deque()
        for r in range(N):
            # pop out all small element from end of deque, as we have new large element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # add new index
            q.append(r)

            # check if l is greater than current max
            if l > q[0]:
                q.popleft()
            
            # check if index has crossed k, then we can get current max from q and add it to res
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res