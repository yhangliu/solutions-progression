class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        left = 0
        right = cols - 1

        while top <= bot:
            mid_row = top + bot - top //2
            first_ele = matrix[mid_row][0]
            last_ele = matrix[mid_row][-1]

            if target < first_ele:
                bot = mid_row - 1
            elif target >= first_ele and target <= last_ele:
                while left <= right:
                    mid_col =left + right - left //2
                    ele = matrix[mid_row][mid_col]
                    if ele == target:
                        return True
                    elif target < ele:
                        right = mid_col -1
                    else:
                        left = mid_col + 1
                return False
            else:
                top = mid_row + 1
        return False
        