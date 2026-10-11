class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        def dfs(row, col):
            if (row < 0 or row >= len(grid)
            or col < 0 or col >= len(grid[0])):
                return
            if grid[row][col] == '1':
                grid[row][col] = '0'
            else:
                return
            for direction in directions:

                dfs(row + direction[0], col +direction[1])
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count

        