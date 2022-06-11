class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # ingredient to recipe mapping in graph and recipe to ingredient count in degree
        # q --> supplies
        # As the supplies in q are explored, deduce recipe count in degree by one and if is 0 append in q and in result 
        result = []
        graph = defaultdict(list)
        degree = defaultdict(int)
        q = deque(supplies)
    
        for recipe, items in zip(recipes,ingredients):
            degree[recipe] = len(items)
            for item in items:
                graph[item].append(recipe)
                
        while q:
            ingredient = q.popleft()
            for rec in graph[ingredient]:
                degree[rec] -= 1
                if degree[rec] == 0:
                    q.append(rec)
                    result.append(rec)
        return result
      
    # O(n*2), O(n)
                    
        
