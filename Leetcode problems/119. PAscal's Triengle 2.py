from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        numRows += 1
        for i in range(numRows-1):
            answer.append([1])
            for j in range(i):

                answer[i].append(answer[-2][j] + answer[-2][j+1])

            answer[i].append(1)

        if numRows:
            answer.insert(0, [1])
        else:
            return []
        return answer[numRows-1]

s = Solution()

print(s.generate(0))