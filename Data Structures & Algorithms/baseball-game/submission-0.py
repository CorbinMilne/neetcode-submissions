class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        record = []

        for i in range(len(operations)):
            if operations[i] not in ['+', 'D', 'C']:
                record.append(int(operations[i]))
            elif operations[i] == '+':
                record.append(record[-1] + record[-2])
            elif operations[i] == 'D':
                record.append(2 * record[-1])
            elif operations[i] == 'C':
                record.pop()

        for i in range(len(record)):
            res += record[i]

        return res



        