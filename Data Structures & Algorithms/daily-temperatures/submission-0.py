class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                output[previous_day] = i - previous_day
            
            stack.append(i)

        return output
                