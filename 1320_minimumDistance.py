class Solution:
    def minimumDistance(self, word: str) -> int:
        # 1) assign each alpha a integer from a range between 0 and 25 inclusive.
        # 2) Derive distance formula to find distance between figures' positions
        # 3) 
        
        W = [ord(w)-65 for w in word] #ord()--> returns unicode code of char
        
        def dist(u,v): 
            return abs(u//6 - v//6) + abs(u % 6 - v % 6)
        
        fcache, tcache, I = {(W[0], -1):0}, {}, math.inf
        
        # `fcache` is the dict object as key as tuple of (position of figure1, position of figure2) and value as the accumulated distance after movement. We initialized it to {(W[0], -1):0} which means the first figure is moving to W[0] and second figure to be -1 as not set yet. The accumulated distance is 0.
        # Below is the DP solution to keep track of movement from either figure1 or figure2
        
        for w in W[1:]:
            for (f1, f2), cdist in fcache.items():
                
                # Movement from fingure 1
                tcache[(w, f2)] = min(tcache.get((w, f2), I), cdist + dist(f1, w))
                
                # Movement from fingure 2
                tcache[(f1, w)] = min(tcache.get((f1, w), I), cdist + (f2 != -1) * dist(f2, w))
            fcache, tcache = tcache, {}
        # Return the minimum accumulated distance
        return min(fcache.values())
    
    # O(n)
