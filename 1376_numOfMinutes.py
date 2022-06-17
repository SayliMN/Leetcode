class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 1) map each value in manager to it's indices in a list name graph
        # 2) in dfs, iterate over each value of key, max(dfs(value) + informTime[key], ans)
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        def dfs(a):
            ans = 0
            for j in graph[a]:
                ans = max(dfs(j) + informTime[a], ans)
            return ans
        return dfs(headID)
    
    # O(n),O(n)
