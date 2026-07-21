class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append([r,c])
            grid[r][c] = "2" #visited

            while q:
                curr_row, curr_col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr = curr_row + dr
                    nc = curr_col + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1":
                        q.append([nr,nc])
                        grid[nr][nc] = "2"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands

        