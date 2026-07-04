class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(row) and nc in range(col) and grid[nr][nc] == "1":
                        grid[nr][nc] = "2"
                        q.append((nr,nc))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    grid[r][c] = "2"  # marked of visited
                    dfs(r,c)
                    islands += 1

        for r in range(row):
            print(grid[r])
        return islands


        