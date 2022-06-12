# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        graph = collections.defaultdict(list) #Time: O(N) and Space: O(N)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.left: # Time: O(1)
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
                
            if node.right: # Time: O(1)
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        
        result = []
        visited = set([target])
        queue = collections.deque([(target,0)]) #Time: O(N) and Space: O(N)
        
        while queue: 
            node, distance = queue.popleft()
            
            if distance == k:
                result.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge,distance+1))
                    
        return result
    
    # Time: O(N)
    # Space: O(N)
