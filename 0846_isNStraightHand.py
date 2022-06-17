class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for n in sorted(count):
            if count[n] > 0:
                need = count[n]
                for i in range(n, groupSize+n):
                    if count[i] < need:
                        return False
                    count[i] -= need
        return True
    
    # O(nlogn)
    
    
