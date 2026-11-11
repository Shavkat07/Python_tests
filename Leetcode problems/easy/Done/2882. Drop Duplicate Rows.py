import pandas as pd

data = {'customer_id': [1, 2, 3, 4, 5, 6], 'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
        'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com',
                  'john@example.com', 'alice@example.com']}


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
	customers.drop_duplicates(subset=['email'], keep='first', inplace=True)
	return customers


print(dropDuplicateEmails(pd.DataFrame(data)))