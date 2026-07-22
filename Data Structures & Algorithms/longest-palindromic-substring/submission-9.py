class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd, even =0, 0 #record the result of palindrome with odd and even length respectively
        odd_res, even_res = "", "" # initialize the result

        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > odd:
                    odd = r-l+1
                    odd_res = s[l:r+1]
                l, r = l-1, r+1
        
        for i in range(len(s)-1): # careful for the r=i+1 not to make indext out of bound
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > even:
                    even = r-l+1
                    even_res = s[l:r+1]
                l, r = l-1, r+1
        
        return odd_res if odd>even else even_res