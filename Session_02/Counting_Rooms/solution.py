def helper(grid, i, j):
    grid[i][j] = "#"
    if i+1 < len(grid) and grid[i+1][j] == '.':
        helper(grid, i+1, j)
    if i > 0 and grid[i-1][j] == '.':
        helper(grid, i-1, j)
    if j+1 < len(grid[0]) and grid[i][j+1] == '.':
        helper(grid, i, j+1)
    if j > 0 and grid[i][j-1] == '.':
        helper(grid, i, j-1)

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

ans=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            ans += 1
            helper(grid, i, j)
            
print(ans)
