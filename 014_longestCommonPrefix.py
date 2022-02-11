        # Space:    O(1)
        # Time:     O(nm)
        # 1) Shortest word in strs 
        # 2) every time I iterate through the shortest word, I will compare every alpha of shortest with every alpha of other words
        # 3) If an particular alpha does not match with shortest, return the alphas till ith count
        
        shortest = min(strs, key=len)
        if strs:
            for i in range(len(shortest)):
                if any(word[i] != shortest[i] for word in strs):
                    return shortest[:i]
            return shortest
        return ""
