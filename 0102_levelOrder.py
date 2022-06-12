# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [] 
        if not root:
            return levels
        
        queue = collections.deque([root]) # not root val but whole tree as in dictionary within dictionary 
        
        while queue:
            length_queue = len(queue)
            currentlevel = []
            for i in range(length_queue):
                node = queue.popleft() # initially all node values will be there, then as per left and right subtree
                currentlevel.append(node.val)
                if node.left:
                    queue.append(node.left) # appending discovered a left node into queue which later will be explored
                if node.right:
                    queue.append(node.right)
            levels.append(currentlevel)
        return levels
    
    # O(N) --> the node is processed exactly once
    # O(N) --> to keep the output of N node values
        
