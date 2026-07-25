class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = [(num, num & 1) for num in nums]

        return [x[0] for x in sorted(arr, key = lambda x: x[1])]