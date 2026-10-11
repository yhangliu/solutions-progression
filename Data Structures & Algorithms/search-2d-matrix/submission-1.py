class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][cols-1]:
                left = 0
                right = cols -1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[mid_row][mid] == target:
                        return True
                    elif target > matrix[mid_row][mid]:
                        left = mid + 1
                    else:
                        right = mid -1
                return False
            elif target >= matrix[mid_row][0]:
                top = mid_row + 1
            else:
                bot = mid_row - 1
        return False

        