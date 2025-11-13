import pandas as pd


data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}



def selectData(students: pd.DataFrame) -> pd.DataFrame:
	res = students.loc[students["student_id"] == 101, ["name", "age"]]
	return res

print(selectData(pd.DataFrame(data)))