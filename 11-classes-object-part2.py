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

>>> 
>>> class Student():
	def __init__(self, i, n):
		self.i = i
		self.n = n
	def __repr__(self):
		return "Student[{},{}]".format(self.i, self.n)

	
>>> s1 = Student(1, "Steve")
>>> s1
Student[1,Steve]
>>> a = "Hello"
>>> s2 = Student(1, "Steve")
>>> 
>>> a = 1000
>>> b = 1000
>>> a == b
True
>>> s1 == s2
False
>>> id(s1), id(s2)
(1807349314440, 1807354398088)
>>> s3 = s1
>>> s3 == s1
True
>>> s3 == s2
False
>>> id (s1), id(s2), id(s3)
(1807349314440, 1807354398088, 1807349314440)
>>> li = [Student("1", "A"), Student("2", "B"), Student("3", "C")]
>>> li
[Student[1,A], Student[2,B], Student[3,C]]
>>> n = [1,2,3]
>>> n.remove(2)
>>> n
[1, 3]
>>> li
[Student[1,A], Student[2,B], Student[3,C]]
>>> li.remove(Student("2","B"))
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    li.remove(Student("2","B"))
ValueError: list.remove(x): x not in list
>>> a= 1000
>>> b = 1000
>>> id(a), id(b)
(1807354580464, 1807354580208)
>>> a == b
True
>>> class Student():
	def __init__(self, i, n):
		self.i = i
		self.n = n
	def __repr__(self):
		return "Student[{},{}]".format(self.i, self.n)
	def __eq__(self, other):
		return self.i == other.i and self.n == other.n

	
>>> s1 = Student(1, "Steve")
>>> s2 = Student(1, "Steve")
>>> id(s1), id(s2)
(1807354479688, 1807354540936)
>>> s1 == s2
True
>>> s2 = Student(1, "Stevie")
>>> s1 == s2
False
>>> s1 == s2
False
>>> s1 = Student(1, "Steve")
>>> s2 = Student(1, "Steve")
>>> s1 == s2
True
>>> s1.__eq__(s2)
True
>>> Student.__eq__(s1,s2)
True
>>> #bmw.drive() --> Car.drive(bmw)
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> int.__eq__(a,b)
True
>>> a == b
True
>>> a = -12
>>> abs(a)
12
>>> len(li)
3
>>> 
>>> li = ['Will','Steve','Aditya']
>>> for item in li:
	print(item)

	
Will
Steve
Aditya
>>> for item in enumerate(li):
	print(item)

	
(0, 'Will')
(1, 'Steve')
(2, 'Aditya')
>>> for idx, name in enumerate(li):
	print(idx, name)

	
0 Will
1 Steve
2 Aditya
>>> for idx, name in enumerate(li):
	print(idx+1, name)

	
1 Will
2 Steve
3 Aditya
>>> li
['Will', 'Steve', 'Aditya']
>>> st = [  Student(i,n) for i, n in enumerate(li)]
>>> st
[Student[0,Will], Student[1,Steve], Student[2,Aditya]]
>>> st = [  Student(i+1,n) for i, n in enumerate(li)]
>>> st
[Student[1,Will], Student[2,Steve], Student[3,Aditya]]
>>> type(st[0])
<class '__main__.Student'>
>>> st[0].i, st[0].n
(1, 'Will')
>>> 
>>> 
>>> st
[Student[1,Will], Student[2,Steve], Student[3,Aditya]]
>>> sorted(st)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    sorted(st)
TypeError: '<' not supported between instances of 'Student' and 'Student'
>>> sorted(st, key = lambda student : student.n)
[Student[3,Aditya], Student[2,Steve], Student[1,Will]]
>>> sorted(st, key = lambda student : student.i)
[Student[1,Will], Student[2,Steve], Student[3,Aditya]]
>>> 
>>> 
>>> fn = ['Bill','Steve','Larry']
>>> 
>>> ln = ['Gates','Jobs','Ellison']
>>> for item in zip(fn,ln):
	print(item)

	
('Bill', 'Gates')
('Steve', 'Jobs')
('Larry', 'Ellison')
>>> for f,l in zip(fn,ln):
	print(f,l)

	
Bill Gates
Steve Jobs
Larry Ellison
>>> fn
['Bill', 'Steve', 'Larry']
>>> ln
['Gates', 'Jobs', 'Ellison']
>>> full_name = [ f + " " + l for f,l in zip(fn,ln)]
>>> full_name
['Bill Gates', 'Steve Jobs', 'Larry Ellison']
>>> 
