class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubseq(s,s[::-1])

    def longestCommonSubseq(self, t1: str, t2: str) -> int:
        dp = [[0 for j in range(len(t2)+1)] for i in range(len(t1)+1)]
        for i in range(len(t1)-1,-1,-1):
            for j in range(len(t2)-1,-1,-1):
                if t1[i] == t2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

        