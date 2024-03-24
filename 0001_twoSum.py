class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

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

        # Time complexity: O(n)
