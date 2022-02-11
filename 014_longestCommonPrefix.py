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


        # Space: O(n)
        # Time: O(1)
        # if I can compare letters in alphabetically largest and smallest words within the string, i can easily get coomon prefix.
        # if the smallest and the largest have the same first alpha, that means the other words must have the first letter in                 common.
        if not strs:
            return ""
        
        mina = min(strs)
        maxa = max(strs)
        
        for i in range(len(mina)):
            if mina[i] != maxa[i]:
                return mina[:i]
        return mina
