class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes =[set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                curr_num = board[row][col]
                if curr_num == ".":
                    continue
                box = ((row//3)*3) + (col // 3)
                if curr_num not in rows[row] and curr_num not in cols[col] and curr_num not in boxes[box]:
                    rows[row].add(curr_num)
                    cols[col].add(curr_num)
                    boxes[box].add(curr_num)
                else:
                    return False



        return True