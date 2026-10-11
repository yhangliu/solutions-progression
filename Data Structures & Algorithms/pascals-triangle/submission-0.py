class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[]for _ in range(numRows)]
        ans[0] = [1] 
        for i in range(1, numRows):
            
            ans[i].append(1)

            for j in range(1, i):
                num = ans[i-1][j] + ans[i-1][j-1]
                ans[i].append(num)
            ans[i].append(1)
        return ans

