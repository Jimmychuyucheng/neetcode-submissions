class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        每一個i只有三個選擇
        1.只選擇自己開頭nums[i]
        2.min_dp[i-1]*nums[i]
        3.max_dp[i-1]*nums[i]
        '''
        res = max(nums)
        curmax, curmin = 1,1
        n = len(nums)

        for i in range(n):
            num = nums[i]
            if num == 0:
                curmax,curmin = 1,1
                continue
            '''
            curmax = max(curmax * num, curmin * num, num)
            curmin = min(curmin * num, curmin * num, num)
            '''
            tmp = curmax * num
            curmax = max(curmax * num, curmin * num, num)
            curmin = min(tmp, curmin * num, num)
            res = max(res, curmax)

        return res
        