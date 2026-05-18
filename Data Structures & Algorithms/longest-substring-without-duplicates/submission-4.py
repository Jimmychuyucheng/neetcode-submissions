class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0,0
        maxL = 0

        hashset = set()

        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1

            hashset.add(s[r])
            maxL = max(maxL, r-l+1)
            r+=1
            
        return maxL




            


        