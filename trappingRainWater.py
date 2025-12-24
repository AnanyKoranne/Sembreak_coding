def trap(height):
    lmax = 0
    rmax = 0
    n = len(height)
    l = 0
    r = n - 1
    ans = 0

    while l < r:
        lmax = max(lmax, height[l])
        rmax = max(rmax, height[r])

        if lmax < rmax:
            ans += lmax - height[l]
            l += 1
        else:
            ans += rmax - height[r]
            r -= 1

    return ans

# Example usage:
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))  # Output: 6    