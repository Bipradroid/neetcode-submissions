class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        maxarea=0

        def bfs(r,c):
            currarea=0
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                dirs=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in dirs:
                    if ((row + dr) in range(rows) and
                        (col+dc) in range(cols) and
                        grid[row+dr][col+dc]==1 and
                        (row+dr,col+dc) not in visit):
                        currarea+=1
                        q.append((row+dr,col+dc))
                        visit.add((row+dr,col+dc))
            return currarea
                

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    curr=bfs(r,c)
                    maxarea=max(maxarea,curr+1)
                    
        return maxarea
