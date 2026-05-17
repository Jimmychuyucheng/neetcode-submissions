class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #O(nlogn)
        lst = []
        for i in range(len(nums)-2): #第一個到倒數第三個
            left = i+1
            right = len(nums)-1

            if i>0 and nums[i] == nums[i-1]: continue
            complement = -nums[i] #nums[i]+complement=0
            while left < right:      
                if nums[left] + nums[right] == complement:
                    r = [nums[left], nums[i], nums[right]]
                    r.sort()
                    lst.append(r)
                    left +=1
                    right -=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1

                elif nums[left] + nums[right] < complement: 
                    left += 1
                else:
                    right -= 1
        return lst
0,0,0,0        


        