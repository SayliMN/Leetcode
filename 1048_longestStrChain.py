class Solution:
    def longestStrChain(self, words: List[str]) -> int:
      # Bottom-up approach
        # 1) words in an array should be sorted by len
        # 2) find a predecessors for each word by iterating through, first an array word by word, mapping word to count=1 in dictionary and then through the word letter by letter
        # 3) find predecessor 
        # 4) if predecessor is in dict and the dp[word] < dp[predecessor] + 1, update dp[word] = dp[predecessor]+1
        # 5) find maximum
        
        dp = {}
        result = 0
        words.sort(key=len)
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp and dp[word] < dp[predecessor] + 1:
                    dp[word] = dp[predecessor] + 1
            result = max(result, dp[word])
        return result
    
    # Time: O(NlogN + N*L*L), where N <= 1000 is number of words, L <= 16 is length of a word
    # Space: O(N)
