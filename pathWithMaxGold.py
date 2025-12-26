def getMaximumGold(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_gold = 0

    def dfs(r, c, current_gold):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return current_gold

        original = grid[r][c]
        grid[r][c] = 0  # mark visited

        gold_up = dfs(r - 1, c, current_gold + original)
        gold_down = dfs(r + 1, c, current_gold + original)
        gold_left = dfs(r, c - 1, current_gold + original)
        gold_right = dfs(r, c + 1, current_gold + original)

        grid[r][c] = original  # backtrack

        return max(gold_up, gold_down, gold_left, gold_right)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                max_gold = max(max_gold, dfs(i, j, 0))

    return max_gold

if __name__ == "__main__":
    grid1 = [
        [0, 6, 0],
        [5, 8, 7],
        [0, 9, 0]
    ]

    grid2 = [
        [1, 0, 7],
        [2, 0, 6],
        [3, 4, 5],
        [0, 3, 0],
        [9, 0, 20]
    ]

    print("Max gold (grid1):", getMaximumGold(grid1))
    print("Max gold (grid2):", getMaximumGold(grid2))
