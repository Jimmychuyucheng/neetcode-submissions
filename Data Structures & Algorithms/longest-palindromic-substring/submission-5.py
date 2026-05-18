class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        # 用來記錄歷史最長迴文的起始與結束索引
        # 預設為第一個字元 (0, 0)
        start, end = 0, 0
        
        # 1. 奇數長度中心擴散
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 如果目前的長度大於歷史最大長度
                if (r - l) > (end - start):
                    start, end = l, r
                l -= 1
                r += 1

        # 2. 偶數長度中心擴散
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 如果目前的長度大於歷史最大長度
                if (r - l) > (end - start):
                    start, end = l, r
                l -= 1
                r += 1

        # 最後要 return 的時候，全程式只做這唯一一次切片
        # 因為切片是左閉右開，所以右邊界要 +1
        return s[start : end + 1]