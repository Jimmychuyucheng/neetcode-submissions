class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res = 1000
        while l<=r:
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
            
            m = l + (r-l)//2
            res = min(res, nums[m])
            if nums[l] <= nums[m]: # left portion is sorted then the min appears in another right portion
                l = m+1
            else:
                r = m-1

        return res

        