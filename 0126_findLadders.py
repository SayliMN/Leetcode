class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        q = deque([[beginWord]])
        visited = set()
        wordSet = set(wordList)
        
        while q:
            curLayerWords = set()
            for _ in range(len(q)):
                curList = q.popleft()
                lastWord = curList[-1]
                if lastWord == endWord:
                    ans.append(curList)
                
                for i in range(len(beginWord)):
                    for c in string.ascii_lowercase:
                        neig = lastWord[:i] + c + lastWord[i+1:]
                        if neig in wordSet and neig not in visited:
                            q.append(curList + [neig])
                            curLayerWords.add(neig)
            visited.update(curLayerWords)
        return ans
    
    # O(n*m*m*26), 
                
    
        
        
