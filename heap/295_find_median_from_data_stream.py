# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# Difficulty: Hard
#
# Implement the MedianFinder class that supports adding integers and
# finding the median of all elements added so far.

class MedianFinder:
    def __init__(self):

        self.small, self.large = [], []

        def addNum(self, num:int) -> None:
            heapq.heappush(small, -1 * num)

            if (small and large and (-1 * self.small[0]) > self.large[0]):
                val = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            if len(small) > len(large) + 1:
                val = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            if len(large) > len(small) + 1:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, val)


        

        def findMedian(self) -> float:
            if len(small) > len(large):
                return self.small[0]
            if len(large) > len(small):
                return self.large[0]
            
            return (self.small[0] + self.large[0])/2

