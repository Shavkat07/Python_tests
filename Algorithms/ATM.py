from abc import ABC, abstractmethod


class ATM(ABC):
	
	@abstractmethod
	def deposit(self, amount_list):
		pass
	
	@abstractmethod
	def withdraw(self, amount):
		pass


class CustomATM(ATM):
	def __init__(self):
		self.kassa = {}
	
	def deposit(self, amount_list):
		for i in range(len(amount_list)):
			if amount_list[i] not in self.kassa:
				self.kassa[amount_list[i]] = 1
			else:
				self.kassa[amount_list[i]] += 1
	
	def withdraw(self, amount):
		valutas = sorted(self.kassa.keys())
		valutas.reverse()
		i = 0
		while i < len(valutas):
			if amount > valutas[i] and self.kassa[valutas[i]] > 0:
				amount -= valutas[i]
				self.kassa[valutas[i]] -= 1
				print(valutas[i], end=", ")
				continue
			i+=1
		if amount > 0:
			print(f"Qoldiq {amount}")
				
atm = CustomATM()
dpst = [5000, 10000, 5000, 5000, 50000, 100000, 100000, 10000]
atm.deposit(dpst)
atm.withdraw(178000)
# print(atm.kassa)
