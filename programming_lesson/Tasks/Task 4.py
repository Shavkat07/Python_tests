"""
Task 4. Undo Text Editor
"""

operations = [
    "ADD H",
    "ADD i",
    "ADD !",
    "UNDO",
    "PRINT"
]


def undo_text_editor(ops: list[str]) -> str:
	ops_stack = []

	for i in ops:
		if i.startswith("ADD "):
			ops_stack.append(i.split()[-1])
		
		if i.startswith("UNDO"):
			ops_stack.pop()

		if i.startswith("PRINT"):
			return "".join(ops_stack)
	
	return "There is no PRINT option"


print(undo_text_editor(operations))