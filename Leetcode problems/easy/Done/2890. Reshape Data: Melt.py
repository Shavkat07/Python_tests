import pandas as pd

data = pd.DataFrame({'product': ['Umbrella', 'SleepingBag'], 'quarter_1': [417, 800], 'quarter_2': [224, 936], 'quarter_3': [379, 93], 'quarter_4': [611, 875]})
# print(data.columns[1::])

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
	
	result = report.melt(
		id_vars='product',
		var_name='quarter',
		value_name='sales'
	)
	
	return result



print(meltTable(data))