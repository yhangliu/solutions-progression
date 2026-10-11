class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def dfs(row, col):
            if (row < 0 or
                col < 0 or
                row >= len(grid) or
                col >= len(grid[0])):
                return 0
            if grid[row][col] != 1:
                return 0
            else:
                grid[row][col] = 0
            area = 1
            area += dfs(row+1,col)
            area += dfs(row-1,col)
            area += dfs(row,col+1)
            area += dfs(row,col-1)
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(max_area, area)


        return max_area