class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] -> 湊到i coin需要的最少硬幣; base case: dp[0]=0
        # dp[i] = min(dp[i-coin]+1) for coin in coins
        dp = [float("inf")]* (amount+1)  #要求的是最小值 defaulf要設定成最大
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[amount] if dp[amount]!= float("inf") else -1