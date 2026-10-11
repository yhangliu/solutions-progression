class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        count = 0
        def dfs(row, col):
            if (row < 0 or 
                col < 0 or 
                row >= len(grid) or
                col >= len(grid[0]) or
                grid[row][col] != "1"):
                return
            grid[row][col] = "0"

            for dr, dc in directions:
                dfs(row + dr, col + dc)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    stack = [[i,j]]
                    while stack:
                        row, col = stack.pop()
                        if (row < 0 or 
                            col < 0 or 
                            row >= len(grid) or
                            col >= len(grid[0]) or
                            grid[row][col] != "1"):
                            continue
                        grid[row][col] = "0"

                        for dr, dc in directions:
                            dfs(row + dr, col + dc)
                    count += 1
        

        return count

        