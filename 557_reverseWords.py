# Approach 1: 
        
        return ' '.join(s.split()[::-1])[::-1]
    
        # Appraoch 2: with for loop
        
        return ' '.join(x[::-1] for x in s.split())
    
        # Time Complexity: O(n)
        # Space Complexity: O()
        
