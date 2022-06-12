class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1) Find patterns for each word in the list and map the pattern to word in dictionary neighbor
        # 2) Explore neigbors pattern in for loop --> for neiword in neighbors[pattern] for each pattern --> range(len(word))
        # 3) if neiword is NOT in visited, append in q and add in visited
        if endWord not in wordList:
            return 0
        
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
                
        result = 1
        q = deque([beginWord])
        visited = set([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbors[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            
            result += 1
        return 0
                
        
        # O(n**2 * m), O(n**2 * m); m --> len(word), n --> len(wordList)
        
        
            
            
        
        
