class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)] # count: 0 to n
        hashmap = {}
        res = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for num, count in hashmap.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res


        