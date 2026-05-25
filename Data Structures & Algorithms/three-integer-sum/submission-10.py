class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2:
            l,r=i+1, len(nums)-1
            while l < r:
                target = 0 - nums[i]
                if nums[l]+nums[r] < target:
                    l+=1
                elif nums[l]+nums[r] > target:
                    r-=1
                else: #nums[l]+nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i+=1
        return res
