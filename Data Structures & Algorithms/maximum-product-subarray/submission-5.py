class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmax, currmin = 1, 1
        n = len(nums)

        for num in nums:
            if num == 0:
                currmax, currmin = 1, 1
                continue
            
            tmp = currmax * num
            currmax = max(currmin * num, currmax * num, num)
            currmin = min(currmin * num, tmp, num)
            res = max(res, currmax)
        return res
            
        
        
        