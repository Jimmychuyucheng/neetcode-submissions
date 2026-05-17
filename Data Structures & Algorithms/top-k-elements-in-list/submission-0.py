class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for num, frequency in hashmap.items():
            buckets[frequency].append(num)

        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        return res #avoid list not full
                    

# [1,2,2,3,3,3] k=2
# hashset{1:1, 2:2, 3:3}
# i=6 5 .... i=3
# hash[num==3] == 3 
# res[3] k=1
# k=1
# i=2 hash[num==2]==2
# res[3,2] k=0