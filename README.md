# 2D Dynamic Programming

Step-by-step practice of **2D Dynamic Programming in Python**, focusing on grid-based problems, DP states, base cases, and state transitions.

## Problems Covered

| # | Problem          | Main Concept     |
| - | ---------------- | ---------------- |
| 1 | Unique Paths     | Grid-based 2D DP |
| 2 | Minimum Path Sum | Grid-based 2D DP |

## 1. Unique Paths

Find the number of possible paths from the starting cell to the destination in a grid.

### DP Approach

A 2D `dp` table is used to store the number of ways to reach each cell.

The first row and first column are initialized with `1`.

For the remaining cells:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

The current cell gets paths from the **top** and **left** cells.

## 2. Minimum Path Sum

Find the minimum cost required to reach the destination of a grid.

### DP Approach

A 2D `dp` table is used to store the minimum cost to reach each cell.

For each cell, the minimum value from the **top** and **left** cells is considered.

```text
dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])
```

The first row and first column are handled separately because they have only one possible direction of movement.

## Key Concepts

* 2D DP Table
* Grid Traversal
* Base Cases
* State Transition
* Top and Left States
* Boundary Handling
* Time and Space Complexity

## Learning Progress

Problems are added step by step while preparing for **DSA and coding interviews**.


