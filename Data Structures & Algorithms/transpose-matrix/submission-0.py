class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(matrix))] for _ in range (len(matrix[0]))]

        for row in range(len(ans)):
            for col in range(len(ans[0])):
                ans[row][col] = matrix[col][row]
        return ans