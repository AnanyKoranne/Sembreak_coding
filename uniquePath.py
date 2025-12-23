def uniquePaths(m, n):
    dp = [1] * n  # first row is all 1s

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[-1]

# Example usage:
if __name__ == "__main__": 
    m = 3
    n = 7
    print(uniquePaths(m, n))  # Output: 28