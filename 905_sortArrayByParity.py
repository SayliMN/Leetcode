class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         1) if l = odd and r = even; swap
#         2) if l = even; l += 1
#         3) if r = odd; r -= 1
        
#         Time: O(n)
#         Space: O(1)

        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] % 2 == 0:
                l += 1
                
            if nums[r] % 2 == 1:
                r -= 1 
                
        return nums
