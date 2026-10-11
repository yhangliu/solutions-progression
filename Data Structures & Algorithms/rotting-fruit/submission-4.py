class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append([row,col])
        if fresh == 0:
            return 0
        minute = 1
        while q:
            for _ in range(len(q)):
                curr_row, curr_col = q.popleft()

                for dr, dc in directions:
                    if (curr_row + dr < 0 or
                        curr_row + dr >= len(grid) or
                        curr_col + dc < 0 or
                        curr_col + dc >= len(grid[0]) or
                        grid[curr_row + dr][curr_col + dc] != 1):
                        continue
                    grid[curr_row + dr][curr_col + dc] = 2
                    q.append([curr_row + dr, curr_col + dc])
                    fresh -= 1
            if fresh == 0:
                return minute
            minute += 1
        return -1
        
            



        