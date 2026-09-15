class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count_hashmap[n] = 1 + count_hashmap.get(n, 0)
        for n, c in count_hashmap.items():
            freq[c].append(n) # value n occurs c amount of times
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

