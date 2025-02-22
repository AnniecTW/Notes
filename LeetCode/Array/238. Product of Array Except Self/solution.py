class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        answer = [1] * n

        for i in range(n):
            prefix[i+1] = nums[i] * prefix[i]
            suffix[i+1] = nums[n-i-1] * suffix[i]

        for i in range(n):
            answer[i] = prefix[i] * suffix[n-i-1]

        return answer

# Below is an optimized solution, solving the problem in O(1) extra space complexity
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        curr = 1
        
        # compute prefix products
        for i in range(n):
            answer[i] *= curr
            curr *= nums[i]

        # compute suffix product and update answer directly
        curr = 1
        for i in range(n-1, -1, -1):
            answer[i] *= curr
            curr *= nums[i]
            
        return answer
