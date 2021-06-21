#классы
class A:
	def g(self): #атрибут self должен присутствовать во всех экземплярах
		return 'Hello World!'
	def hl(self):
		return 'Hell'
	#инкапсуляция:
	def _private(self):
		print("Приватный метод")

a=A()
print(a.g())
print(a.hl())
print(a._private())
#наследование:
class Mydict(dict):
	def get(self, key, default=0):
		return dict.get(self, key, default)


c1=dict(a=1, b=2)
b=Mydict(a=1, b=2)
print(c1)
print(b)
#полиморфизм:
#1. перегрузка операторов:
class AB:
	def go(self):
		print("Go, AB!")
class BA(AB):
	def go(self, name):
		print('Go, {}!'.format(name))
#создание экземляра класса-конструктор
#метод __init__ перегружает конструктор класса
class H:
	def __init__(self, name):
		self.name=name
#	def __add__(self):
a=H('Vlad')
print(a.name)