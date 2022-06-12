class Solution:
  def rob2(self, nums:list[int]) -> int:
    if not nums or len(nums) == 0:
      return 0
   
    return max(self.helper(nums[1:]), self.helper(nums[:-1], nums[0])
    
#     [rob1, rob2, n, n+1, ...]
  def helper(self, nums):
    rob1, rob2 = 0, 0
    for n in nums:
      temp = max(rob1+n, rob2)
      rob1 = rob2
      rob2 = temp
    return rob2
               
#   O(n),O(1)
    
