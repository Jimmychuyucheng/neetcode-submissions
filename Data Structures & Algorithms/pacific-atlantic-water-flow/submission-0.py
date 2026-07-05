class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set() # record the visited node
        row, col = len(heights), len(heights[0])

        def dfs(r,c,visit,prevheight):
            if (r,c) in visit or r<0 or r==row or c<0 or c==col or heights[r][c] < prevheight:
                return
            
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visit, heights[r][c])
        
        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col-1]) 

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row-1, c, atl, heights[row-1][c])

        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))

        return res

        