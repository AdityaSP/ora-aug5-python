Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> class Car():
	pass

>>> bmw = Car()
>>> type(bmw)
<class '__main__.Car'>
>>> dir(bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> bmw.brand = 'BMW'
>>> dir(bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand']
>>> bmw.brand
'BMW'
>>> bmw.name='X4'
>>> dir(bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'name']
>>> bmw.brand, bmw.name
('BMW', 'X4')
>>> honda = Car()
>>> dir(honda)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> honda.name = 'City'
>>> honda.brand = 'Honda'
>>> dir(honda)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'name']
>>> 
>>> 
>>> 
>>> 
>>> class Car():
	def __init__(self):
		print("in here")
		print(id(self))

		
>>> bmw = Car()
in here
1979130305480
>>> id(bmw)
1979130305480
>>> class Car():
	def __init__():
		print("in here")

		
>>> bmw = Car()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    bmw = Car()
TypeError: __init__() takes 0 positional arguments but 1 was given
>>> class Car():
	def __init__(self):
		print("in here")
		print(id(self))

		
>>> bmw = Car()
in here
1979125658632
>>> class Car():
	def __init__(self):
		self.brand = 'BMW'
		self.name = 'X4'

		
>>> bmw = Car()
>>> dir(bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'name']
>>> bmw.brand
'BMW'
>>> bmw.name
'X4'
>>> honda = Car()
>>> honda.brand, honda.name
('BMW', 'X4')
>>> class Car():
	def __init__(self, b, n):
		self.brand = b
		self.name = n

		
>>> bmw = Car()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    bmw = Car()
TypeError: __init__() missing 2 required positional arguments: 'b' and 'n'
>>> bmw = Car('BMW','X4')
>>> honda = Car('Honda','City')
>>> bmw.brand, bmw.name
('BMW', 'X4')
>>> honda.brand, honda.name
('Honda', 'City')
>>> 

>>> 
""" In C++/Java a class def would look like this
class A {
	
		
		String name;
		String brand;
		A (String n, String b){
			this.name = n
			this.name = b
		}
	}
We would declare what data attributes we want and later define then in a constructor. Where as python cannot declare variables. So it has to compose them"""
' In C++/Java a class def would look like this\nclass A {\n\t\n\t\t\n\t\tString name;\n\t\tString brand;\n\t\tA (String n, String b){\n\t\t\tthis.name = n\n\t\t\tthis.name = b\n\t\t}\n\t}\nWe would declare what data attributes we want and later define then in a constructor. Where as python cannot declare variables. So it has to compose them'
>>> 
