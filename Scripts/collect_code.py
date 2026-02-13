import os


def collect_code_to_file(output_filename="consolidated_code.py", exclude_files=None, exclude_dirs=None):
	if exclude_files is None:
		exclude_files = [output_filename, os.path.basename(__file__)]  # Исключаем сам скрипт и файл результата
	if exclude_dirs is None:
		exclude_dirs = {'.git', '__pycache__', '.venv', 'venv', 'env', '.idea', '.vscode'}
	
	project_root = os.getcwd()
	
	with open(output_filename, 'w', encoding='utf-8') as outfile:
		for root, dirs, files in os.walk(project_root):
			# Убираем скрытые и ненужные папки из обхода
			dirs[:] = [d for d in dirs if d not in exclude_dirs]
			
			for file in files:
				# Берем только Python файлы (можно добавить и другие расширения)
				if file.endswith('.py') and file not in exclude_files:
					full_path = os.path.join(root, file)
					relative_path = os.path.relpath(full_path, project_root)
					
					try:
						with open(full_path, 'r', encoding='utf-8') as infile:
							code = infile.read()
							
							# Пишем заголовок-комментарий
							outfile.write(f"\n{'#' * 80}\n")
							outfile.write(f"# SOURCE FILE: {relative_path}\n")
							outfile.write(f"{'#' * 80}\n\n")
							
							# Пишем сам код
							outfile.write(code)
							outfile.write("\n\n")
						
						print(f"Добавлен: {relative_path}")
					except Exception as e:
						print(f"Ошибка при чтении {relative_path}: {e}")
	
	print(f"\nГотово! Весь код собран в файл: {output_filename}")


if __name__ == "__main__":
	collect_code_to_file()