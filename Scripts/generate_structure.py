import os
from pathlib import Path


def create_structure():
	# Определяем корневую структуру
	# Ключи словаря - это папки, списки - это файлы внутри.
	# Если значение словаря - это вложенный словарь, значит это подпапка.
	
	structure = {
		"alembic": [],  # Папка для миграций
		"app": {
			"__init__.py": "",
			"core": {
				"__init__.py": "",
				"config.py": "# Переменные окружения и настройки\n",
				"security.py": "# Логика JWT и хеширования\n",
				"database.py": "# Настройка сессии PostgreSQL\n",
			},
			"modules": {
				"__init__.py": "",
				"auth": {
					"__init__.py": "",
					"models.py": "",
					"schemas.py": "",
					"service.py": "",
					"router.py": "",
				},
				"finance": {
					"__init__.py": "",
					"models.py": "",
					"schemas.py": "",
					"router.py": "",
				},
				"social": {
					"__init__.py": "",
					"models.py": "",
					"schemas.py": "",
					"logic_gap.py": "# Логика для Gap (Гап)\n",
					"router.py": "",
				},
				"analytics": {
					"__init__.py": "",
					"ml_service.py": "# Загрузка моделей (CatBoost/Pandas)\n",
					"zakat.py": "# Расчет Zakat\n",
					"router.py": "",
				},
			},
			"utils": {
				"__init__.py": "",
				"sms_parser.py": "# Парсер SMS (Click, Payme)\n",
				"currency.py": "# Курсы валют\n",
			},
			"main.py": "# Точка входа FastAPI\nfrom fastapi import FastAPI\n\napp = FastAPI()\n",
		},
		"ml_models": [],  # Папка для .cbm/.pkl
		"tests": {
			"__init__.py": "",
		},
		".env": "DB_URL=postgresql://user:pass@localhost/db\nSECRET_KEY=supersecret\n",
		"requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nalembic\npydantic\npython-dotenv\npandas\ncatboost\npytest\n",
		"docker-compose.yml": "version: '3.8'\nservices:\n  db:\n    image: postgres:15\n",
	}
	
	base_path = Path.cwd()  # Создаст в текущей директории
	
	print(f"🚀 Создание структуры проекта в: {base_path}")
	
	def build_tree(base, tree):
		for name, content in tree.items():
			path = base / name
			
			if isinstance(content, dict):
				# Это папка
				path.mkdir(exist_ok=True)
				print(f"📁 Создана папка: {path.relative_to(base_path)}")
				build_tree(path, content)
			elif isinstance(content, list):
				# Это папка (пустая или с файлами, заданными списком - для alembic/ml_models)
				path.mkdir(exist_ok=True)
				print(f"📁 Создана папка: {path.relative_to(base_path)}")
			elif isinstance(content, str):
				# Это файл
				with open(path, "w", encoding="utf-8") as f:
					f.write(content)
				print(f"📄 Создан файл:  {path.relative_to(base_path)}")
	
	build_tree(base_path, structure)
	print("\n✅ Структура проекта успешно создана!")


if __name__ == "__main__":
	create_structure()