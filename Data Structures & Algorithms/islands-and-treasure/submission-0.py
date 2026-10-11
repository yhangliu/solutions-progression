class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row,col])
        distance = 0
        while(q):
            distance += 1
            to_explore = len(q)
            for _ in range(to_explore):
                curr_row, curr_col = q.popleft()
                for row_inc, col_inc in directions:
                    test_row = curr_row + row_inc
                    test_col = curr_col + col_inc
                    if test_row >= rows or test_row < 0 or test_col >= cols or test_col <0:
                        continue  
                    if grid[test_row][test_col] == 2147483647:
                        grid[test_row][test_col] = distance
                        q.append([test_row, test_col])

                        


        