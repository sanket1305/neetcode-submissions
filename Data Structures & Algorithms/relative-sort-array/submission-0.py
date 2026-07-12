class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapp = {}

        for i, num in enumerate(arr2):
            mapp[num] = i
        
        arr = []
        for i, num in enumerate(arr1):
            if num in mapp:
                arr.append((mapp[num], num))
            else:
                arr.append((10**5, num))
        
        arr.sort()

        return [y for x, y in arr]