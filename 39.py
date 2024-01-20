class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def traverse(candid, arr, sm):
            if sm == target:
                self.result.append(arr)
            if sm >= target:
                return
            for i in range(len(candid)):
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])
        traverse(candidates, [], 0)
        return self.result
