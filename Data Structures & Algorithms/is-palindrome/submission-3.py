class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        lst=[]
        for i in s: 
            if 0 <= ord(i) - ord('a') < 26 or 0 <= ord(i) - ord('0') < 9:
                lst.append(i)
        print(lst)
        l = 0
        r = len(lst)-1
        while l <= r:
            if lst[l] == lst[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            

