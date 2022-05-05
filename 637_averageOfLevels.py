# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        if not root:
            return levels
        
        queue = collections.deque([root])
        while queue:
            currentlevelsum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                currentlevelsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            currentlevelsum /= i + 1
            levels.append(currentlevelsum)
        return levels
    
#     O(n) --> each node will be processed exactly once
#     O(n) --> queue size          
                
