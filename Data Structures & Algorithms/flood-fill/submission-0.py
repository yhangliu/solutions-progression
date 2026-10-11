class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        q = deque()
        start = image[sr][sc]
        q.append((sr,sc))
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        while q:
            row, col = q.pop()
            if (row,col) in visited:
                continue
            image[row][col] = color
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if(
                    new_row >= 0 and
                    new_row < len(image) and
                    new_col >= 0 and
                    new_col < len(image[0])
                ):
                    if image[new_row][new_col] == start:
                        q.append((new_row,new_col))
            visited.add((row,col))


        return image