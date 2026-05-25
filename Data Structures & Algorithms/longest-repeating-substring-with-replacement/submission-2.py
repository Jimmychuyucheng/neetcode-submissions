class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        maxf = 0
        hashmap = {}
            

        l,r=0,0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxf = max(maxf, hashmap[s[r]])
            while (r-l+1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1

        return res
            
        