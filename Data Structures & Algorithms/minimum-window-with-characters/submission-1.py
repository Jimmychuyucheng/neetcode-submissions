class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=r=0
        res = [-1,-1]
        reslen = float("infinity")
        countS = {}
        countT = {}
        for st in t:
            countT[st] = 1 + countT.get(st,0)

        have = 0
        need = len(countT)

        while r < len(s):
            countS[s[r]] = 1 + countS.get(s[r],0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]: # not >=
                have += 1
            while need == have:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r+1]
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
            r+=1

            
        left, right = res[0], res[1]
        return s[left:right] if s else ""