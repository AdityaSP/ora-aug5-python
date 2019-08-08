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
>>> 
>>> 
>>> # Classes, Objects, Data encapsulation
>>> class Car():
	def __init__(self, b, n):
		self.brand = b
		self.name = n
	def drive(self):
		print("I drive a ", self.brand, self.name)

		
>>> bmw = Car('BMW','X4')
>>> dir(bmw)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'brand', 'drive', 'name']
>>> bmw.drive()
I drive a  BMW X4
>>> s = 'hello'
>>> s.upper()
'HELLO'
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> class Car():
	def __init__(self, b, n):
		self.brand = b
		self.name = n
		self.miles = 0
	def drive(self, miles):
		self.miles += miles

		
>>> bmw = Car('BMW','X4')
>>> bmw.drive(50)
>>> bmw.miles
50
>>> bmw.drive(150)
>>> bmw.miles
200
>>> # Classes, objects, encapsulation
>>> s = 'Hello'
>>> s
'Hello'
>>> bmw
<__main__.Car object at 0x000001CCCD659608>
>>> class Car():
	def __init__(self, b, n):
		self.brand = b
		self.name = n
		self.miles = 0
	def drive(self, miles):
		self.miles += miles
	def __str__(self):
		return "Car({},{},{})".format(self.brand, self.name, self.miles)

	
>>> bmw = Car('BMW','X4')
>>> bmw.drive(50)
>>> bmw.drive(50)
>>> bmw
<__main__.Car object at 0x000001CCCD630348>
>>> print(bmw)
Car(BMW,X4,100)
>>> class Car():
	def __init__(self, b, n):
		self.brand = b
		self.name = n
		self.miles = 0
	def drive(self, miles):
		self.miles += miles
	def __str__(self):
		return "Car({},{},{})".format(self.brand, self.name, self.miles)
	def __repr__(self):
		return self.__str__()

	
>>> bmw = Car('BMW','X4')
>>> bmw
Car(BMW,X4,0)
>>> print(bmw)
Car(BMW,X4,0)
>>> bmw.drive(50)
>>> bmw
Car(BMW,X4,50)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class LB():
	def breathe():
		print("I breathe")

		
>>> class LB():
	def breathe(self):
		print("I breathe")

		
>>> lb = LB()
>>> lb.breathe()
I breathe
>>> class HB():
	def breathe(self):
		print("I breathe")

		
>>> # is-a relationship
>>> # is LB a HB
>>> # is HB a LB
>>> class LB():
	def breathe(self):
		print("I breathe")

		
>>> class HB(LB):
	pass

>>> hb= HB()
>>> hb.breathe()
I breathe
>>> class Fabric():
	def breathe(self):
		print("I breathe")

		
>>> dir(hb)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'breathe']
>>> class LB():
	def breathe(self):
		print("I breathe")

		
>>> class HB(LB):
	def metathink(self):
		print(" I think therefore I am ")

		
>>> hb = HB()
>>> hb.breathe()
I breathe
>>> hb.metathink()
 I think therefore I am 
>>> 
>>> 
>>> 
>>> 
>>> class Fish(LB):
	def breathe(self):
		print("through gills")

		
>>> 
>>> f = Fish()
>>> f.breathe()
through gills
>>> # Overriding
>>> class LB():
	def breathe(self):
		print("I breathe")

		
>>> class Fish(LB):
	def breathe(self):
		LB.breathe(self)
		print("through gills")

		
>>> f = Fish()
>>> f.breathe()
I breathe
through gills
>>> 
>>> 
>>> 
>>> 
>>> class A():
	def __init__(self):
		self.v1 = 10
	def report(self):
		print(self.v1)

		
>>> class B(A):
	def __init__(self):
		self.v2 = 20

		
>>> obj = B()
>>> obj.v2
20
>>> dir(obj)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'report', 'v2']
>>> obj.report()
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    obj.report()
  File "<pyshell#166>", line 5, in report
    print(self.v1)
AttributeError: 'B' object has no attribute 'v1'
>>> class A():
	def __init__(self):
		self.v1 = 10
	def report(self):
		print(self.v1)

		
>>> class B(A):
	def __init__(self):
		A.__init__()
		self.v2 = 20

		
>>> obj = B()
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    obj = B()
  File "<pyshell#178>", line 3, in __init__
    A.__init__()
TypeError: __init__() missing 1 required positional argument: 'self'
>>> class B(A):
	def __init__(self):
		A.__init__(self)
		self.v2 = 20

		
>>> obj = B()
>>> dir(obj)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'report', 'v1', 'v2']
>>> obj.report()
10
>>> isinstance(obj, B)
True
>>> issubclass(B, A)
True
>>> issubclass(A, B)
False
>>> 
