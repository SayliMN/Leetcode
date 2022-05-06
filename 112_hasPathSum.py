# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Recursive DFS
        # Time: O(N) --> we are vising the node exactly once
        # Space: O(logN) --> in imbalanced tree (with only one child), storage to keep the call stack would be O(N) but in balanced tree, O(logN) height
        # if not root:
        #     return False
        # if root.val == targetSum and not root.left and not root.right:
        #     return True
        # return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
        # Iterative DFS
        # Time: O(N) --> we are vising the node exactly once
        # Space: O(logN) --> in imbalanced tree (with only one child), storage to keep the call stack would be O(N) but in balanced tree, O(logN) height
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
        return False
                
