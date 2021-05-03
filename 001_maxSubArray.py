class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        #KADANE ALGORITHM
        GM = LM = nums[0]
        for i in range(1, n):
            LM = max(LM+nums[i], nums[i])
            GM = max(LM, GM)
        return GM
