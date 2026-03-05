import os
import re
from pathlib import Path


def create_structure_from_tree(tree_input: str, base_path: Path):
	print(f"🚀 Создание структуры проекта в: {base_path}\n")
	
	# Разбиваем на строки и убираем пустые
	lines = tree_input.strip('\n').split('\n')
	nodes = []
	
	# 1. Парсим строки
	for line in lines:
		if line.strip() == '.' or not line.strip():
			continue  # Пропускаем корневую директорию "."
		
		# Нормализуем пробелы (защита от неразрывных пробелов при копировании)
		clean_line = line.replace('\xa0', ' ')
		
		# Вычленяем чистое имя (удаляем символы веток и пробелы слева)
		name = re.sub(r'^[\s│├└─|\\\-]+', '', clean_line)
		if not name:
			continue
		
		# Считаем глубину вложенности.
		# Каждые 4 символа префикса в tree (например, "├── " или "│   ") — это 1 уровень
		prefix = clean_line[:clean_line.find(name)]
		depth = len(prefix) // 4
		
		nodes.append({'depth': depth, 'name': name, 'is_dir': False})
	
	# 2. Определяем, папка это или файл (Эвристика)
	for i in range(len(nodes)):
		# Если следующий элемент находится глубже, значит текущий элемент — это папка
		if i + 1 < len(nodes) and nodes[i + 1]['depth'] > nodes[i]['depth']:
			nodes[i]['is_dir'] = True
		else:
			# Если вложенности нет, смотрим на название
			# Есть расширение (точка) или это специфичный файл -> Файл
			if '.' in nodes[i]['name'] or nodes[i]['name'] in ['Dockerfile', 'Makefile']:
				nodes[i]['is_dir'] = False
			else:
				nodes[i]['is_dir'] = True  # Пустые папки без расширения (напр. alembic, ml_models)
	
	# 3. Физическое создание структуры
	# Стек путей для отслеживания родительских папок на каждом уровне
	path_stack = {0: base_path}
	
	for node in nodes:
		# Родительская папка всегда находится на уровне (depth - 1)
		parent_path = path_stack.get(node['depth'] - 1, base_path)
		current_path = parent_path / node['name']
		
		# Обновляем стек текущим путем, чтобы его "дети" могли к нему привязаться
		path_stack[node['depth']] = current_path
		
		if node['is_dir']:
			current_path.mkdir(parents=True, exist_ok=True)
			print(f"📁 Создана папка: {current_path.relative_to(base_path)}")
		else:
			current_path.parent.mkdir(parents=True, exist_ok=True)
			current_path.touch()
			print(f"📄 Создан файл:  {current_path.relative_to(base_path)}")
	
	print("\n✅ Структура успешно сгенерирована!")


if __name__ == "__main__":
	# Просто вставь сюда вывод команды tree
	TREE_INPUT = """
fastapi-project
├── alembic/
├── src
│   ├── auth
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── dependencies.py
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── aws
│   │   ├── client.py  # client model for external service communication
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   └── posts
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   ├── pagination.py  # global module e.g. pagination
│   ├── database.py  # db connection related stuff
│   └── main.py
├── tests/
│   ├── auth
│   ├── aws
│   └── posts
├── templates/
│   └── index.html
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
"""

	create_structure_from_tree(TREE_INPUT, Path.cwd())