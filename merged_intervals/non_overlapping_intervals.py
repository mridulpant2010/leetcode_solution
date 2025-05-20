
import heapq
class Solution:
    
    def eraseOverlapIntervals(self,intervals):
        he = []
        for el in intervals:
            # Push (end, start) so heap pops the earliest ending interval
            heapq.heappush(he, (el[1], el[0]))

        count = 0
        # Pop the first interval
        end, start = heapq.heappop(he)
        while he:
            next_end, next_start = heapq.heappop(he)
            if next_start <= end:
                # Overlap, need to remove this interval
                count += 1
            else:
                # No overlap, update end
                end = next_end
        return count


if __name__=="__main__":
    s = Solution()
    intervals = [[1,2],[2,3],[3,4],[4,5]]#[[1,2],[3,4],[5,6],[7,8]]# [[10,16],[2,8],[1,6],[7,12]]#[[1,2],[2,4],[1,4]]
    res=s.eraseOverlapIntervals(intervals)
    print(res)