class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                p = merged[-1][1]
                ct = intervals[i][0]
                ce = intervals[i][1]
                if p >= ct:
                    merged[-1][1] = max(p,ce)
                else:
                    merged.append(intervals[i])

        return merged
