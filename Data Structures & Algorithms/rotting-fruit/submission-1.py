class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=collections.deque()
        count=0
        fresh=0
        
        def bfs(r,c):
            nonlocal fresh
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or grid[r][c]==2 ):
                return
            
            grid[r][c]=2
            fresh-=1
            q.append([r,c])
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                elif grid[r][c]==1:
                    fresh+=1
                    
        
        while q and fresh>0:
            for _ in range(len(q)):
                row,col=q.popleft()
                
                bfs(row+1,col)
                bfs(row-1,col) 
                bfs(row,col+1)
                bfs(row,col-1)
            count+=1
        if fresh>0:
            return -1
        return count



        