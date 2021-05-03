class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                sum_1 = nums[i] + nums[j]
                if sum_1 == target:
                    return i, j 
