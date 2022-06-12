# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        queue = collections.deque([root])
        while queue:
            currentLevel = []
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.insert(0, currentLevel)
        return levels
    
    # O(n) --> the node will be process exactly once
    # O(n) --> n nodes will be kept in the result
