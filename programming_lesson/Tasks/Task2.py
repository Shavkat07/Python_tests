"""
Task 2. Remove Adjacent Duplicates
"""

s = "abbaca"


def adj_dpc(word: str) -> str:
	stack = []
	for i in s:
		if len(stack) == 0 or stack[-1] != i:
			stack.append(i)
		else:
			stack.pop()

	return "".join(stack)


print(adj_dpc(s))
