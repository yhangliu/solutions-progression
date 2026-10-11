class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        def dfs(row, col):
            if( row < 0 or 
                col < 0 or 
                row >= len(grid) or
                col >= len(grid[0]) or
                grid[row][col] == 0):
                return 0
            grid[row][col] = 0
            count = 1
            for dr, dc in directions:
                count += dfs(row + dr, col + dc)
            return count
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area,dfs(row,col))
        return max_area

        