# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth
        
        queue = collections.deque([root])
        while queue:
            depth += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        # O(n) --> 
        # O(n)
