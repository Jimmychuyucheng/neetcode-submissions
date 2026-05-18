class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        if s[i]=0 dp[i]=0
        if s[i]=1 dp[i]=dp[i+1]+dp[i+2] 
        if s[i]=2 and 0<=i+1<7 dp[i]=dp[i+1]+dp[i+2] else dp[i]=dp[i+1]
        if s[i]=3-9 dp[i]=dp[i+1]
        '''
        n = len(s)
        dp = [0]* (n+2) #開到n+1處理dp[i+2]的邊界情況
        dp[n] = 1

        for i in range(n-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            
            elif s[i]=="1":
                dp[i] = dp[i+1] + dp[i+2]

            elif s[i]=="2":
                if i+1 <= n-1 and 0 <= int(s[i+1]) < 7: #20-26
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]

            else:
                dp[i] = dp[i+1]

        return dp[0]


        