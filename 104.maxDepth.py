# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            height_left = self.maxDepth(root.left)
            height_right = self.maxDepth(root.right)
            return max(height_left, height_right) + 1
        
        # Time: O(n)
        # Space: O(lon(n))
