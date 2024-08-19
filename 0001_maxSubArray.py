class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # Kadane Algorithm
        LM = GM = nums[0]
        for i in range(1, n):
            LM = max(LM + nums[i], nums[i])
            GM = max(LM, GM)
        return GM

# Time complexity: O(n)
# Space complexity: O(1)
