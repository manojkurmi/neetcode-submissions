class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        islands = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            if grid[r][c] == "0" or visited[r][c]:
                return

            visited[r][c] = True
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                dfs(r + dr, c + dc)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and not visited[r][c]:
                    islands += 1
                    dfs(r, c)

        return islands