class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while len(q) != 0 and fresh > 0:
            time +=1
            total_len = len(q)
            for _ in range(total_len):
                i, j = q.popleft()
                for dx, dy in [[-1,0], [1,0], [0,1], [0,-1]]:
                    new_i = i + dx
                    new_j = j + dy
                    if new_i < 0 or new_j < 0 or new_i == rows or new_j == cols:
                        continue
                    if grid[new_i][new_j] == 0 or grid[new_i][new_j] == 2:
                        continue
                    fresh -=1
                    grid[new_i][new_j] = 2
                    q.append([new_i, new_j])
        if fresh > 0:
            return -1
        else:
            return time


        