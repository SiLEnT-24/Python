# <!-- A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is **valid** if **any** of the following conditions is **true**:

# - It is `()`.
# - It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
# - It can be written as `(A)`, where `A` is a valid parentheses string.

# You are given an `m x n` matrix of parentheses `grid`. A **valid parentheses string path** in the grid is a path satisfying **all** of the following conditions:

# - The path starts from the upper left cell `(0, 0)`.
# - The path ends at the bottom-right cell `(m - 1, n - 1)`.
# - The path only ever moves **down** or **right**.
# - The resulting parentheses string formed by the path is **valid**.

# Return `true` *if there exists a **valid parentheses string path** in the grid.* Otherwise, return `false`.

# **Example 1:**

# [image](https://assets.leetcode.com/uploads/2022/03/15/example1drawio.png)

# ```
# Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# Output: true
# Explanation: The above diagram shows two possible paths that form valid parentheses strings.
# The first path shown results in the valid parentheses string "()(())".
# The second path shown results in the valid parentheses string "((()))".
# Note that there may be other valid parentheses string paths.

# ```

# **Example 2:**

# [image](https://assets.leetcode.com/uploads/2022/03/15/example2drawio.png)

# ```
# Input: grid = [[")",")"],["(","("]]
# Output: false
# Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

# ```

# **Constraints:**

# - `m == grid.length`
# - `n == grid[i].length`
# - `1 <= m, n <= 100`
# - `grid[i][j]` is either `'('` or `')'`. -->

class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string has even length
        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        memo = set()

        def dfs(i, j, balance):
            if i >= m or j >= n:
                return False

            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            if (i, j, balance) in memo:
                return False

            if dfs(i + 1, j, balance):
                return True

            if dfs(i, j + 1, balance):
                return True

            memo.add((i, j, balance))
            return False

        return dfs(0, 0, 0)

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []

for i in range(m):
    row = input(f"Enter row {i+1}: ").strip()
    if len(row) != n or any(c not in "()" for c in row):
        raise ValueError("Invalid row")
    grid.append(list(row))


obj = Solution()
print(obj.hasValidPath(grid))