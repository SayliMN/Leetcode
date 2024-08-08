class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:           
        dictionary = {}
        for i, v in enumerate(nums):
            comp = target - nums[i]
            if comp in dictionary:
                return (dictionary[comp],i)
            dictionary[nums[i]] = i

        # Time complexity: O(n)
