class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        
        # 建立一個二維 DP 表，初始化皆為 False
        dp = [[False] * n for _ in range(n)]
        # 單個字元一定是迴文
        for i in range(n):
            dp[i][i] = True
            
        start, max_len = 0, 1
        
        # 開始從小區間推導到大區間
        for length in range(2, n + 1): # 子字串長度
            for i in range(n - length + 1):
                j = i + length - 1 # 右邊界
                
                if s[i] == s[j]:
                    if length == 2: # 長度為 2 且字元相同，一定是迴文
                        dp[i][j] = True
                    else:           # 長度大於 2，看剝掉外殼後的中間是不是迴文
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length
                    
        return s[start:start + max_len]


                



        