from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 傳統死板的 DP 寫法 (空間複雜度 O(n))
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])  # 狀態轉移
        return max(dp)
       