class Solution:
  
    def trap(self, height: List[int]) -> int:
        max_h_left, max_h_right, water = 0, 0, 0
        max_h = 0
        max_h_ind = 0
        
        for i in range(len(height)):
            if height[i] > max_h:
                max_h = max(height[i],max_h)
                max_h_ind = i
        
        for j in range(max_h_ind):
            max_h_left = max(height[j], max_h_left)
            water += max_h_left - height[j]
            
        for l in range(len(height)-1, max_h_ind,-1):
            max_h_right = max(height[l], max_h_right)
            water += max_h_right - height[l]
        
        return water

# Space complexity: O(1)
# Time complexity: O(n)
  
