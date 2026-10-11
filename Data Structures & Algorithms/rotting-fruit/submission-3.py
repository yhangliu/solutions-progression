class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append([row,col])
                elif grid[row][col] == 1:
                    fresh += 1
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            if fresh == 0:
                return time
            cells = len(q)
            for _ in range(cells):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row = dr + row
                    new_col = dc + col
                    if (new_row < 0 or
                        new_row >= rows or
                        new_col < 0 or
                        new_col >= cols):
                        continue
                    if grid[new_row][new_col] == 1:
                        fresh -= 1
                        grid[new_row][new_col] = 2
                        q.append([new_row,new_col])
            time += 1
            
        if fresh > 0:
            return -1
        return time


        