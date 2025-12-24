from functools import cache

def uniquePaths(m: int, n: int) -> int:
    
    @cache
    def backtrack(r, c):
        # Base case
        if r == m - 1 and c == n - 1:
            return 1
        
        paths = 0
        
        # Move down
        if r < m - 1:
            paths += backtrack(r + 1, c)
        
        # Move right
        if c < n - 1:
            paths += backtrack(r, c + 1)
        
        return paths
    
    # Start from top-left corner
    return backtrack(0, 0)

# Example usage:
if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths(m, n))  # Output: 28