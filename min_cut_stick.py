class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        cuts.insert(0, 0)
        cuts.append(n)
        n = len(cuts)

        dp = [[0] * n for _ in range(n)]

        for diagonal in range(2, n):
            for i in range(n - diagonal):
                j = i + diagonal
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

                dp[i][j] += cuts[j] - cuts[i]

        return dp[0][n - 1]