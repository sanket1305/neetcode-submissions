from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        res = []

        idx = bisect_left(arr, x)

        left, right = idx - 1, idx
        while k:
            if left >= 0 and right < n:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            else:
                if left >= 0:
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            k -= 1
        
        return sorted(res)