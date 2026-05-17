from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        curSub = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            curSub = max(curSum, curSub)
        
        return curSub
       