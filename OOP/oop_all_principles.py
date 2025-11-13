from abc import ABC, abstractmethod  # для абстракции



class Person(ABC):
	def __init__(self, name: str, age: int, iq: int = 75):
		
		self._name = name
		self.__age = age
		self._iq = iq
	
	@property
	def age(self):
		return self.__age
	
	@age.setter
	def age(self, value):
		if value > 0:
			self.__age = value
		else:
			raise ValueError("Возраст должен быть положительным")
	

	@abstractmethod
	def iq(self):
		pass
	
	def info(self):
		print(f"Name: {self._name}, Age: {self.__age}, IQ: {self._iq}")



class Scientist(Person):
	def __init__(self, name, age, field):
		super().__init__(name, age, iq=150)
		self.field = field
	
	def iq(self):
		print(f"{self._name} — Scientist, IQ: {self._iq}, Field: {self.field}")
	
	def research(self):
		print(f"{self._name} is researching in {self.field}")


class Worker(Person):
	def __init__(self, name, age, job):
		super().__init__(name, age, iq=60)
		self.job = job
	
	def iq(self):
		print(f"{self._name} — Worker, IQ: {self._iq}, Job: {self.job}")
	
	def work(self):
		print(f"{self._name} is working as a {self.job}")


class Student(Person):
	def __init__(self, name, age, major):
		super().__init__(name, age, iq=100)
		self.major = major
	
	def iq(self):
		print(f"{self._name} — Student, IQ: {self._iq}, Major: {self.major}")
	
	def study(self):
		print(f"{self._name} is studying {self.major}")


people = [
	Scientist("Einstein", 40, "Physics"),
	Worker("Bob", 30, "Builder"),
	Student("Alice", 20, "Computer Science")
]

for person in people:
	person.info()
	person.iq()
	print()
