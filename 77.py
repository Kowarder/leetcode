class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]
        result = []
        if n == 1:
            return [[1]]
        else:
            s = itertools.combinations(arr, k)
            for i in s:
                result.append(i)
            return result
