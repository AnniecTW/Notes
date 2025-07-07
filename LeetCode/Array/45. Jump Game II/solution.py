class Solution:
    def jump(self, nums: List[int]) -> int:
        last = len(nums) - 1
        jumps, curEnd, farthest = 0, 0, 0
        
        for i in range(last):
            farthest = max(farthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = farthest
                if curEnd >= last:
                    break
            
        return jumps
