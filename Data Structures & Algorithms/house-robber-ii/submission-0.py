class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:len(nums)-1]))
        

    def helper(self, nums) :  
        rob1, rob2 = 0, 0
        #[rob1, rob2, n,  n+1, ....]
        for n in nums:
            tmp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2

# [1,1,3,3]
# rob1=0 rob2=0 
# n=1 tmp=1 rob1=0 rob2=tmp=1
# n=1 tmp=1 rob1=1 rob2=1
# n=3 tmp=4 rob1=1 rob2=4
# n=3 tmp=4 rob1=4 rob2=4
# return rob2       