class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt = 1
        points.sort()
        pend = points[0][1]
        for start, end in points[1:]:
            if start<=pend:
                pend = min(end,pend)
            else:
                cnt+=1
                pend = end
        return cnt
