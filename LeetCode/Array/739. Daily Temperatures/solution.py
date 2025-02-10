class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [0]
        n = len(temperatures)
        answers = [0] * n
        for i in range(1, n):
            while s and temperatures[i] > temperatures[s[-1]]:
                    index = s.pop()
                    answers[index] = i - index
            s.append(i)
        return answers
