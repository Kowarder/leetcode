class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        for j in range(len(ratings)-2,-1, -1):
            if ratings[j+1] < ratings[j]:
                candy[j] = max(candy[j], candy[j+1] + 1)
        return sum(candy)
