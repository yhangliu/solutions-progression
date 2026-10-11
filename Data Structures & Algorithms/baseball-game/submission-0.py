class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        scores = []

        for op in operations:
            if op == "+":
                add = scores[-1] + scores[-2]
                scores.append(add)
                ans += add
            elif op == "D":
                double = scores[-1] * 2
                scores.append(double)
                ans += double
            elif op == "C":
                sub = scores.pop()
                ans -= sub
            else:
                scores.append(int(op))
                ans += int(op)
        return ans
        