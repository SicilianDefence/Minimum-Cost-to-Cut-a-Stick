# Minimum Cost to Cut a Stick
1. The function minCost takes two parameters: n, which represents the length of the stick, and cuts, which is a list of the positions where the stick should be cut.
The cuts list is sorted in ascending order to ensure consistency.
2. 0 is inserted at the beginning of the cuts list, and n is appended at the end. This accounts for the starting and ending positions of the stick, making it easier to calculate the cost.
3. The variable n is reassigned to the length of the modified cuts list.
4. A 2D list, dp, is initialized with all elements set to 0. This list will be used to store the minimum cost of cutting the stick between various positions.
5. A nested loop iterates over the dp list, starting from the diagonal element dp[0][2] (since n is initially set to 3) and moving diagonally upwards.
6. For each diagonal element dp[i][j], the inner loop (k) iterates over the range from i+1 to j-1, representing the possible cut positions between i and j. The minimum cost is calculated by finding the minimum of the current value of dp[i][j] and the sum of the minimum costs of cutting the stick between i and k and between k and j.
7. Finally, the minimum cost of cutting the stick from the starting position 0 to the ending position n-1 is returned as dp[0][n-1].

![min_cost](https://github.com/SicilianDefence/Minimum-Cost-to-Cut-a-Stick/assets/45375601/572bda2c-c395-40f6-957b-b230acd0dc50)
