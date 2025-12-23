def table_to_dict(table_str: str):
	"""
	Принимает скопированный текст DataFrame из задачи и возвращает
	Python-словарь с данными (подходит для создания pandas DataFrame).
	"""
	lines = [line.strip() for line in table_str.strip().split('\n') if line.strip()]
	
	# Находим строки с данными (между линиями +----+)
	data_lines = [line for line in lines if '|' in line and '+' not in line]
	
	# Разбиваем первую строку — это имена колонок
	columns = [col.strip() for col in data_lines[0].split('|')[1:-1]]
	
	# Остальные строки — данные
	rows = []
	for line in data_lines[1:]:
		parts = [part.strip() for part in line.split('|')[1:-1]]
		rows.append(parts)
	
	# Преобразуем в словарь
	data_dict = {col: [] for col in columns}
	
	for row in rows:
		for col, value in zip(columns, row):
			# Преобразуем числа в int если можно
			if value.isdigit():
				value = int(value)
			elif value == 'None':
				value = None
			data_dict[col].append(value)
	
	return data_dict


# ---------------- Пример использования ----------------
table = """
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
"""

data = table_to_dict(table)

print(f'data = pd.DataFrame({data})')
