class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        """
        count = 0
        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        def dfs(row, col):
            if (row < 0 or
                row >= len(grid) or
                col < 0 or
                col >= len(grid[0])):
                return
            if grid[row][col] == "1":
                grid[row][col] = "0"
            else:
                return
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1

        return count
        """

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i,j)]
                    while stack:
                        row, col = stack.pop()
                        if (row < 0 or
                            row >= len(grid) or
                            col < 0 or
                            col >= len(grid[0])):
                            continue
                        if grid[row][col] == "1":
                            grid[row][col] = "0"
                        else:
                            continue
                        for dr, dc in directions:
                            stack.append((row + dr, col + dc))
        return count

                        


        