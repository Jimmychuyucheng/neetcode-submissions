class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd_res, even_res = "", ""
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if len(odd_res) < r-l+1:
                    odd_res = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)): #even
            l, r = i, i+1  #i and i+1 are the center
            while l>=0 and r<len(s) and s[l] == s[r]:
                if len(even_res) < r-l+1:
                    even_res = s[l:r+1]
                l -= 1
                r += 1

        if len(odd_res) > len(even_res): return odd_res
        else: return even_res


                



        