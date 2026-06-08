class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        hash map紀錄每一個字母出現數量
        res - hash map max value < k -> 可以繼續加
        否則l+=1 並且扣掉該元素
        '''
        hashmap = {}
        l,r = 0, 0
        res = 0
        maxf = 0
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0)+1
            maxf = max(maxf, hashmap[s[r]])
            while (r-l+1)-maxf > k:
                hashmap[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1

        return res

                
                
        
        