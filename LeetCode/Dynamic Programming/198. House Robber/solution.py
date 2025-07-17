class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = nums[0]
        skip = 0
        
        n = len(nums)
        for i in range(1, n):
            prev_rob = rob
            rob = skip + nums[i] 
            skip = max(skip, prev_rob)
            
        return max(skip, rob)
