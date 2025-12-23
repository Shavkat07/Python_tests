import random


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def insert(root, value):
	if root is None:
		return Node(value)
	if value < root.value:
		root.left = insert(root.left, value)
	else:
		root.right = insert(root.right, value)
	return root


# --- Самая важная часть: Функция красивой отрисовки ---
def display(node):
	lines, _, _, _ = _display_aux(node)
	for line in lines:
		print(line)


def _display_aux(node):
	"""
	Рекурсивная функция для построения ASCII-графики.
	Возвращает: список строк, ширину, высоту, горизонтальную позицию корня.
	"""
	# 1. Если узла нет - возвращаем пустоту
	if node.right is None and node.left is None:
		line = str(node.value)
		width = len(line)
		height = 1
		middle = width // 2
		return [line], width, height, middle
	
	# 2. Если есть только левый ребенок
	if node.right is None:
		lines, n, p, x = _display_aux(node.left)
		s = str(node.value)
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
		second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
		shifted_lines = [line + u * ' ' for line in lines]
		return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
	
	# 3. Если есть только правый ребенок
	if node.left is None:
		lines, n, p, x = _display_aux(node.right)
		s = str(node.value)
		u = len(s)
		first_line = s + x * '_' + (n - x) * ' '
		second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
		shifted_lines = [u * ' ' + line for line in lines]
		return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
	
	# 4. Если есть оба ребенка (самый частый случай)
	left, n, p, x = _display_aux(node.left)
	right, m, q, y = _display_aux(node.right)
	s = str(node.value)
	u = len(s)
	first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
	second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
	
	if p < q:
		left += [n * ' '] * (q - p)
	elif q < p:
		right += [m * ' '] * (p - q)
	
	zipped_lines = zip(left, right)
	lines = [a + u * ' ' + b for a, b in zipped_lines]
	return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


# --- Функция для создания ИДЕАЛЬНОГО дерева из списка ---
# Она берет середину списка и делает её корнем, чтобы дерево было ровным
def build_balanced_bst(objects):
	if not objects:
		return None
	
	mid = len(objects) // 2
	root = Node(objects[mid])
	
	root.left = build_balanced_bst(objects[:mid])
	root.right = build_balanced_bst(objects[mid + 1:])
	
	return root


# --- ТЕСТИРОВАНИЕ ---

# 1. Генерируем список чисел от 1 до 15
numbers = [random.randrange(1, 100) for _ in range(100)]
# numbers = [1, 2, 3, ... 15]

# 2. Строим правильное дерево (пирамидкой), а не линией
# Если используем обычную вставку
root = Node(numbers[0])
for num in numbers[1:]:
	insert(root, num)

print("Твое дерево (как на картинке):")
print("=" * 50)
display(root)
print("=" * 50)
