# Topic: Dunder methods

############  Exercise No1 ####################################################################
#
# class Fraction:
# 	def __init__(self, num, den):
# 		self.num, self.den = num, den
# 		self._reduce()
#
# 		def _reduce(self):
# 			from math import gcd
# 			g = gcd(self.num, self.den)
# 			self.num //= g
# 			self.den //= g
# 			if self.den < 0:
# 				self.num, self.den = -self.num, -self.den
#
# 	def __add__(self, other):
# 		new_num = self.num * other.den + self.den * other.num
# 		new_den = self.den * other.den
# 		return Fraction(new_num, new_den)
#
# 	def __sub__(self, other):
# 		new_num = self.num * other.den - self.den * other.num
# 		new_den = self.den * other.den
# 		return Fraction(new_num, new_den)
#
# 	def __mul__(self, other):
# 		new_num = self.num * other.num
# 		new_den = self.den * other.den
# 		return Fraction(new_num, new_den)
#
# 	def __truediv__(self, other):
# 		new_num = self.num * other.den
# 		new_den = self.den * other.num
# 		return Fraction(new_num, new_den)
#
# 	def __eq__(self, other):
# 		return self.num == other.num and self.den == other.den
#
# 	def __repr__(self):
# 		return f"Fraction({self.num}, {self.den})"
#
# 	def __str__(self):
# 		return f"{self.num}/{self.den}"
#
# a = Fraction(2, 5)
# b = Fraction(2, 5)
#
# print(a == b)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

############  Exercise No2 ####################################################################

class MyList:
	def __init__(self, data):
		self.data = list(data)
	
	def __len__(self):
		length = 0
		for _ in self.data:
			length += 1
		
		return length
	
	def __getitem__(self, index):

		if index < 0:
			index = len(self.data) + index
		
		i = 0
		for item in self.data:
			if i == index:
				return item
			i += 1
		
		raise IndexError("Index out of range")
	
	def __contains__(self, item):
		for i in self.data:
			if item == i:
				return True
		return False
	

ml = MyList([10, 20,40])

print(ml[1])

############  Exercise No1 ####################################################################





############  Exercise No1 ####################################################################





############  Exercise No1 ####################################################################