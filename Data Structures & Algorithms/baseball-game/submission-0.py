class Solution:
    def calPoints(self, operations: List[str]) -> int:
        fixedOps = ["C", "+", "D"]
        record = []
        for op in operations:
            if op not in fixedOps:
                record.append(int(op))
            elif op == "+":
                record.append(record[-1] + record[-2])
            elif op == "C":
                record.pop()
            else:
                record.append(2 * record[-1])
        
        return sum(record)