class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        
        while queue:
            for _ in range(len(queue)):
                word, length = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            wordList.remove(next_word)
                            queue.append([next_word, length + 1])
        return 0
    
    # Time Complexity: O(n*m*26*m), 
    # Space complexity: O(n*m)
        
        
            
            
        
        
