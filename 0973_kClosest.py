class Solution:
    def kClosest(self, points, k):
        
        heap, euclidean = [], lambda x, y : x*x + y*y
        for i, (x, y) in enumerate(points):
            d = euclidean(x, y)
            if len(heap) == k:
                heappushpop(heap, (-d, i))     # -d to convert to max-heap (default is min)
            else: 
                heappush(heap, (-d, i))
        return [points[i] for (_, i) in heap]
        
        # time complexity: O(nlogk)
        # space complexity: O(k)
