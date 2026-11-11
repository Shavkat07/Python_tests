class HashTable:
	def __init__(self, size):
		self.size = size
		self.buckets = [[] for _ in range(self.size)]
	
	def _hash(self, key):
		hash_value = sum([ord(char) for char in key])
		return hash_value % self.size
	
	def add(self, key, value):
		hash_value = self._hash(key)
		slot = self.buckets[hash_value]
		
		for item in slot:
			if item[0] == key:
				item[1] = value
				return
			
		slot.append([key, value])
		
	def delete(self, key):
		hash_value = self._hash(key)
		slot = self.buckets[hash_value]
		
		# for item in slot:
		# 	if item[0] == key: