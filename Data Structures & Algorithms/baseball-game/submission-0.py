class Solution:
    def calPoints(self, operations: List[str]) -> int:
        count = []

        for op in operations:
            if op == "+":
                count.append(count[-1] + count[-2])
            elif op == "D":
                count.append(count[-1] * 2)
            elif op == "C":
                count.pop()
            else:
                count.append(int(op))
            
        return sum(count)