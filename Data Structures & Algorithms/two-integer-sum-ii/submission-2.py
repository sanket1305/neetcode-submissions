class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)

        lo, hi = 0, N-1
        while lo < hi:
            curSum = numbers[lo] + numbers[hi]

            if curSum < target:
                lo += 1
            elif curSum > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]