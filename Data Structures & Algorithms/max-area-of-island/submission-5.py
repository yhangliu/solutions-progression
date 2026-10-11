class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    area = 0
                    while stack:
                        row, col = stack.pop()

                        if (row < 0 or
                            col < 0 or
                            row >= len(grid) or
                            col >= len(grid[0]) or
                            grid[row][col] == 0):
                            continue
                        area += 1
                        grid[row][col] = 0
                        for dr, dc in directions:
                            stack.append((row + dr, col + dc))
                    max_area = max(max_area, area)
        return max_area
                        
                            
