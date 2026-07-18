class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = {}
        for key, val in count.items():
            if val in freq:
                freq[val].append(key)
            else:
                freq[val] = [key]
        
        for i in range(n, 0, -1):
            if i in freq:
                for num in freq[i]:
                    res.append(num)
                    k -= 1
                    if not k:
                        return res