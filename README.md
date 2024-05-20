# goit-algo-hw-09

Performance Comparison: Greedy vs. Dynamic Programming

Greedy Algorithm (find_coins_greedy):

Complexity: O(n * log(n))
O(n) for iterating through denominations (n being the number of denominations).
O(log(n)) for integer division when calculating the number of coins (worst-case scenario with large amounts).
Performance for Large Sums: While the greedy approach is efficient for finding a solution, it might not be the minimum number of coins for all cases. This can become a significant issue with large sums of money.

Dynamic Programming (find_min_coins):

Complexity: O(amount * n)
O(amount) for iterating through possible amounts.
O(n) for iterating through denominations for each amount.
Performance for Large Sums: Dynamic programming guarantees the optimal solution (minimum number of coins) for all cases. However, the time complexity grows linearly with the amount, which can be slower for very large sums compared to the greedy approach.

Summary:

Greedy Algorithm: Faster for most cases, especially with small sums, but might not be optimal for all scenarios with large sums.
Dynamic Programming: Guaranteed optimal solution, but can be slower for very large sums due to its linear time complexity.