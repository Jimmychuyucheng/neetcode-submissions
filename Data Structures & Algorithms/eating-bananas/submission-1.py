class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # output: 1~max(piles) binary search
        l,r=1,max(piles)
        res = r
        while l<=r:
            m = l + (r-l)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)

            if hours > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)


        return res