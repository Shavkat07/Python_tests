from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame({
	    'student_id': [i[0] for i in student_data],
	    'age': [i[1] for i in student_data],
	    
    })
    
    df2 =pd.DataFrame(student_data, columns=['student_id', 'age'])
    # a = [df.shape[0], df.shape[1]]
    return df

print(createDataframe([
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]))
