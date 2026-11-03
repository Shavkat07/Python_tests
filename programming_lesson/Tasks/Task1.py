"""
Task 1. Browser Navigation
"""

operations = [
	"VISIT google.com",
	"VISIT youtube.com",
	"VISIT github.com",
	"VISIT sldkjf.com",
	"VISIT asdf.com",
	"VISIT lex.uz",
	"BACK",
	"BACK",
	"BACK",
	"FORWARD",
	"FORWARD",
	# "VISIT life.com",
	"CURRENT"
]


def browser_navigation(ops: list[str]) -> str:
	ops_stack = []
	ops_backed_up = []
	for i in ops:
		if i.startswith("VISIT "):
			ops_stack.append(i.split()[-1])
		
		if i.startswith("BACK"):
			x = ops_stack.pop()
			ops_backed_up.append(x)
		
		if i.startswith("FORWARD"):
			if len(ops_backed_up) > 0:
				ops_stack.append(ops_backed_up[-1])
				ops_backed_up.pop()
			
		if i.startswith("CURRENT"):
			return ops_stack[-1]
	
	return "There is no CURRENT option"


print(browser_navigation(operations))
