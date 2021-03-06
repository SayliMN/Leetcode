class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Com plexity: O(n^2)
        # Brute force
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 sum_1 = nums[i] + nums[j]
#                 if sum_1 == target:
#                     return i, j 

        # Complexity:O(n)
        # Found index of element's complement
#         for i, e in enumerate(nums):
#             diff = target - e
#             if (diff in nums) and (i !=nums.index(diff)) :
#                 return [nums.index(diff), i]
           
        dictionary = {}
        for i, v in enumerate(nums):
            comp = target - nums[i]
            if comp in dictionary:
                return (dictionary[comp],i)
            dictionary[nums[i]] = i
