class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        res = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            # remove all smaller elements from the end of the queue
            # as we have new largest element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # add new element idx
            q.append(r)

            # check if l is larger than curr max
            # is so, then curr max is invalid (out of window)
            if l > q[0]:
                q.popleft()
            
            # check if we have crossed kth index, then add res
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res