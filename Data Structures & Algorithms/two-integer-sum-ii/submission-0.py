class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        first, last = 0, n-1
        while first < last:
            diff = target - numbers[last]
            if diff > numbers[first]:
                first += 1
            elif diff < numbers[first]:
                last -= 1
            else:
                return [first + 1, last + 1]
