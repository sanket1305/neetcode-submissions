import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi)//2
            print(lo, hi, mid)

            cur_hrs = 0
            for pile in piles:
                cur_hrs += math.ceil(pile / mid)

            if cur_hrs <= h:
                hi = mid
            else:
                lo = mid +1
            
            print(cur_hrs)
            print(lo, hi)

        return lo