class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = maxSubarray = nums[0]
        for r in nums[1:]:
            l = max(r, r + l)
            maxSubarray = max(maxSubarray, l)
        return maxSubarray
        
        # O(n),O(1)
