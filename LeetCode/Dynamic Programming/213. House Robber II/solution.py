class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(houses):
            rob, skip = 0, 0
            for house in houses:
                rob, skip = skip + house, max(rob, skip)
            return max(rob, skip)
        
        return max(dp(nums[:-1]), dp(nums[1:]))
      
