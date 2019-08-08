Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class A():
	pass

>>> obja = A()
>>> dir(obja)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> class A(object):
	pass

>>> obja = A()
>>> dir(obja)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> obja
<__main__.A object at 0x000001A4CEB78688>
>>> #Python 3 only supports new style classes
>>> # In py 2 class A() --> would mean old style and class A(object) --> would mean new style
>>> 
>>> class Emp():
	def __init__(self,n):
		self.name = n
	def __repr__(self):
		return "Emp({})".format(self.name)

	
>>> e1 = Emp("Bill")
>>> e1.name
'Bill'
>>> e1.name = "B2"
>>> e1
Emp(B2)
>>> #Data Hiding
>>> class Emp():
	def __init__(self,n):
		self.__name = n
	def __repr__(self):
		return "Emp({})".format(self.__name)

	
>>> e1 = Emp("Bill")
>>> e1
Emp(Bill)
>>> e1.name
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    e1.name
AttributeError: 'Emp' object has no attribute 'name'
>>> e1.__name
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    e1.__name
AttributeError: 'Emp' object has no attribute '__name'
>>> e1
Emp(Bill)
>>> class Emp():
	def __init__(self,n):
		self.__name = n
	def __repr__(self):
		return "Emp({})".format(self.__name)
	def get_name(self):
		return self.__name
	def set_name(self, newn):
		return self.__name = newn
	
SyntaxError: invalid syntax
>>> class Emp():
	def __init__(self,n):
		self.__name = n
	def __repr__(self):
		return "Emp({})".format(self.__name)
	def get_name(self):
		return self.__name
	def set_name(self, newn):
		self.__name = newn

		
>>> e1 = Emp("Bill")
>>> e1.get_name()
'Bill'
>>> e1.set_name("William")
>>> e1
Emp(William)
>>> class Emp():
	def __init__(self,n):
		if len(n)<3:
			raise ValueError("too short")
		self.__name = n
	def __repr__(self):
		return "Emp({})".format(self.__name)
	def get_name(self):
		return self.__name
	def set_name(self, newn):
		if len(n)<3:
			raise ValueError("too short")
		self.__name = newn

		
>>> e1 = Emp("Bill")
>>> e2 = Emp("El")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    e2 = Emp("El")
  File "<pyshell#43>", line 4, in __init__
    raise ValueError("too short")
ValueError: too short
>>> e1.set_name("El")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    e1.set_name("El")
  File "<pyshell#43>", line 11, in set_name
    if len(n)<3:
NameError: name 'n' is not defined
>>> class Emp():
	def __init__(self,n):
		if len(n)<3:
			raise ValueError("too short")
		self.__name = n
	def __repr__(self):
		return "Emp({})".format(self.__name)
	def get_name(self):
		return self.__name
	def set_name(self, newn):
		if len(newn)<3:
			raise ValueError("too short")
		self.__name = newn

		
>>> e1 = Emp("Bill")
>>> e2 = Emp("El")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    e2 = Emp("El")
  File "<pyshell#48>", line 4, in __init__
    raise ValueError("too short")
ValueError: too short
>>> e1.set_name("El")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    e1.set_name("El")
  File "<pyshell#48>", line 12, in set_name
    raise ValueError("too short")
ValueError: too short
>>> 
>>> 
>>> 
>>> e1.__name
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    e1.__name
AttributeError: 'Emp' object has no attribute '__name'
>>> dir(e1)
['_Emp__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_name', 'set_name']
>>> e1._Emp__name
'Bill'
>>> # __name ---> became _Emp__name
>>> # Name mangling
>>> e1.__name
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    e1.__name
AttributeError: 'Emp' object has no attribute '__name'
>>> e1._Emp__name
'Bill'
>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> e1 = Emp("Bill")
>>> e1.get_name()
'Bill'
>>> e1.set_name("Will")
>>> e1
Emp(Will)
>>> class Emp():
	def __init__(self,n):
		if len(n)<3:
			raise ValueError("too short")
		self.__name = n
	def __repr__(self):
		return "Emp({})".format(self.__name)
	def get_name(self):
		return self.__name
	def set_name(self, newn):
		if len(newn)<3:
			raise ValueError("too short")
		self.__name = newn
	name = property(get_name, set_name)

	
>>> 
>>> 
>>> e1= Emp("Bill")
>>> e1.name
'Bill'
>>> e1.name = 'El'
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    e1.name = 'El'
  File "<pyshell#77>", line 12, in set_name
    raise ValueError("too short")
ValueError: too short
>>> e1.name = "Will"
>>> e1
Emp(Will)
>>> 
