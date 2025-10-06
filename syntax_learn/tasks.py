a = [1,[2,[3,4],5,],6]
ans = []

def func(lst):
	for i in lst:
		if isinstance(i, list):
			func(lst=i)
		else:
			ans.append(i)
	return ans
	
func(a)
print(ans)

