class Solution:
    def kClosest(self, points, k):
        # return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[0:k]
        # time complexity: O(nlogn)
        # space complexity: O(n)
        
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
