# class MedianFinder:
#     def __init__(self):
#         self.data_stream_arr = []

#     def addNum(self, num):
#         self.data_stream_arr.append(num)
#         self.data_stream_arr.sort()

#     def findMedian(self):
#         if not self.data_stream_arr:
#             return []

#         n = len(self.data_stream_arr)
#         if n % 2 == 1:
#             return self.data_stream_arr[n // 2]
#         else:
#             median1 = n//2
#             median2 = n//2 - 1
#             return (self.data_stream_arr[median1] + self.data_stream_arr[median2]) / 2
    
#     # time: O(nlogn) + O(1)
#     # space: O(n)
import heapq
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
    
    def addNum(self, num):
        # max of small heap should be less than equals to min of large heap elements
        heappush(self.small, -1*num)
        if self.small and self.large and (-1*self.small[0] > self.large[0]):
            val = -1* heappop(self.small)
            heappush(self.large, val)
        
        # uneven size
        if len(self.small) < len(self.large) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        if  len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)    
                   
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (-1*self.small[0] + self.large[0]) / 2

#     def __init__(self):
#         self.small = []  # the smaller half of the list, max heap (invert min-heap)
#         self.large = []  # the larger half of the list, min heap

#     def addNum(self, num):
#         if len(self.small) == len(self.large):
#             heappush(self.large, -heappushpop(self.small, -num))
#         else:
#             heappush(self.small, -heappushpop(self.large, num))

#     def findMedian(self):
#         if len(self.small) == len(self.large):
#             return float(self.large[0] - self.small[0]) / 2.0
#         else:
#             return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
