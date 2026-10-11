class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                box = (3 * (row // 3)) + (col // 3)
                print(box)
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in boxes[box]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)
        return True