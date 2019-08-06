Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # functional styles of programming
>>> # first class objects/first class constructs
>>> a = 10
>>> def sayhi():
	return "Hi"

>>> id(a)
140717282456096
>>> id(sayhi)
1978085238104
>>> type(a)
<class 'int'>
>>> type(sayhi)
<class 'function'>
>>> b = a
>>> id(a), id(b)
(140717282456096, 140717282456096)
>>> type(a), type(b)
(<class 'int'>, <class 'int'>)
>>> greet = sayhi
>>> id(greet), id(sayhi)
(1978085238104, 1978085238104)
>>> type(greet), type(sayhi)
(<class 'function'>, <class 'function'>)
>>> sayhi()
'Hi'
>>> greet()
'Hi'
>>> a = 10
>>> a = 20
>>> def sayhi():
	return "Hello"

>>> id(sayhi)
1978084797752
>>> id(greet)
1978085238104
>>> greet()
'Hi'
>>> sayhi()
'Hello'
>>> def execother(f):
	print(type(f))

	
>>> execother(a)
<class 'int'>
>>> execother(sayhi)
<class 'function'>
>>> def execother(f):
	return f()

>>> execother(sayhi)
'Hello'
>>> execother(greet)
'Hi'
>>> 
>>> 
>>> def add(x,y):
	return x + y

>>> def sub(x,y):
	return x - y

>>> def calc(f, x, y):
	return f(x,y)

>>> calc(add, 4,5)
9
>>> calc(sub, 4,5)
-1
>>> sayhi
<function sayhi at 0x000001CC8F0AAD38>
>>> a
20
>>> sayhi()
'Hello'
>>> # add is a first order function
>>> # calc, execother -> higher order function
>>> 
>>> 
>>> li= ['Adam', 'adrian','ben','John']
>>> sorted(li)
['Adam', 'John', 'adrian', 'ben']
>>> def toupper(s):
	return s.upper()

>>> toupper(l[-1])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    toupper(l[-1])
NameError: name 'l' is not defined
>>> toupper(li[-1])
'JOHN'
>>> toupper(li[-2])
'BEN'
>>> sorted(li, key=toupper)
['Adam', 'adrian', 'ben', 'John']
>>> li = ['aaaa','bbb','cc','z']
>>> def strlen(x):
	return len(x)

>>> sorted(li, key=strlen)
['z', 'cc', 'bbb', 'aaaa']
>>> sorted(li, key=len)
['z', 'cc', 'bbb', 'aaaa']
>>> li = [[5,6,7],[0,8,9],[9,0,0]]
>>> sorted(li)
[[0, 8, 9], [5, 6, 7], [9, 0, 0]]
>>> sum(li[0])
18
>>> sorted(li, key=sum)
[[9, 0, 0], [0, 8, 9], [5, 6, 7]]
>>> sorted(li, key=min)
[[0, 8, 9], [9, 0, 0], [5, 6, 7]]
>>> sorted(li, key=max)
[[5, 6, 7], [0, 8, 9], [9, 0, 0]]
>>> 

>>> 
>>> 
>>> 3
3
>>> 'Hello'
'Hello'
>>> add(3,4)
7
>>> x = 3
>>> y = 4
>>> add(x,y)
7
>>> def toupper(s):
	return s.upper()

>>> sorted(li, key=strlen)
[[5, 6, 7], [0, 8, 9], [9, 0, 0]]
>>> def toupper(s):
	return s.upper()

>>> li= ['Adam', 'adrian','ben','John']
>>> # function literals or anonymous functions
>>> def add(x,y):
	return x + y

>>> 
>>> 
>>> calc(add, 4,5)
9
>>> def add(x,y):
	return x + y

>>> lambda x,y: x+y
<function <lambda> at 0x000001CC8F1713A8>
>>> d = lambda x,y: x+y
>>> d(8,9)
17
>>> def calc(f, x, y):
	return f(x,y)

>>> calc(lambda x,y: x +y, 3,4)
7
>>> calc(lambda x,y: x**2 +y**2, 3,4)
25
>>> sorted(li,key = lambda x: x.upper())
['Adam', 'adrian', 'ben', 'John']
>>> li = [[5,6,7],[0,8,9],[9,0,0]]
>>> 
>>> 
>>> sorted(li)
[[0, 8, 9], [5, 6, 7], [9, 0, 0]]
>>> sorted(li, key = lambda x: x[1])
[[9, 0, 0], [5, 6, 7], [0, 8, 9]]
>>> li = [[5,6,7],[0,0,9],[9,0,0]]
>>> sorted(li, key = lambda x: x[1])
[[0, 0, 9], [9, 0, 0], [5, 6, 7]]
>>> # map and filter
>>> 
>>> 
>>> li = [2,3,4.5]
>>> newli = []
>>> for sal in li:
	newli.appen(sal + sal * 0.15)

	
Traceback (most recent call last):
  File "<pyshell#121>", line 2, in <module>
    newli.appen(sal + sal * 0.15)
AttributeError: 'list' object has no attribute 'appen'
>>> for sal in li:
	newli.append(sal + sal * 0.15)

	
>>> newli
[2.3, 3.45, 5.175]
>>> map(lambda x : x + x * 0.15, li)
<map object at 0x000001CC8F118508>
>>> list(map(lambda x : x + x * 0.15, li))
[2.3, 3.45, 5.175]
>>> sum(map(lambda x : x + x * 0.15, li))
10.925
>>> li = [3,4,5]
>>> list(map(lambda x : x*x , li))
[9, 16, 25]
>>> 
>>> 
>>> ages = [12,34,56,78,89]
>>> list(filter(lambda x: 30<x<60, ages))
[34, 56]
>>> filter(lambda x: 30<x<60, ages)
<filter object at 0x000001CC8F14BEC8>
>>> sum(filter(lambda x: 30<x<60, ages))
90
>>> min(filter(lambda x: 30<x<60, ages))
34
>>> max(filter(lambda x: 30<x<60, ages))
56
>>> list(filter(lambda x: 30<x<60, ages))
[34, 56]
>>> s = '23,45,56'.split(',')
>>> s
['23', '45', '56']
>>> list(map(int, s))
[23, 45, 56]
>>> sum(map(int,s))
124
>>> 
>>> 
>>> def greet():
	def sayhi():
		return "Hi"
	return sayhi

>>> x = greet()
>>> type(x)
<class 'function'>
>>> x()
'Hi'
>>> 
>>> 
>>> def greet(n):
	def sayhi():
		return "Hi " + n
	return sayhi

>>> x = greet('Aditya')
>>> y = greet('Arun')
>>> 
>>> 
>>> type(x), type(y)
(<class 'function'>, <class 'function'>)
>>> # body of x : return Hi Aditya, body of y : return Hi Arun
>>> x()
'Hi Aditya'
>>> y()
'Hi Arun'
>>> # closure --> special higher order function , if the returned function captures a local variable of the parent function
>>> 
>>> 
>>> 
>>> def bill(item1, item2, tax):
	total = item1 + item2
	grandtotal = total + total * tax
	return grandtotal

>>> bill (100, 200, .05)
315.0
>>> def bill(item1, item2):
	total = item1 + item2
	def withtax(tax):
		return total+ total * tax
	return withtax

>>> b1 = bill(100,200)
>>> type(b1)
<class 'function'>
>>> b1(0.05)
315.0
>>> bill(10,20)(0.1)
33.0
>>> def f1(i1,i2):
	def f2(t):
		return (i1+ i2) + (i1+i2)* t
	def f3(t):
		return (i1+ i2) + (i1+i2)* 2*t
	if i1 > 1000 or i2 > 1000:
		return f3
	else
	
SyntaxError: invalid syntax
>>> def f1(i1,i2):
	def f2(t):
		return (i1+ i2) + (i1+i2)* t
	def f3(t):
		return (i1+ i2) + (i1+i2)* 2*t
	if i1 > 1000 or i2 > 1000:
		return f3
	else:
		return f2

	
>>> x = f1(1000,2000)
>>> x(.1)
3600.0
>>> y = f1(100,200)
>>> y(.1)
330.0
>>> 
>>> # Decorators
>>> 
>>> 
>>> def sayhi():
	print("Hi")

	
>>> sayhi()
Hi
>>> def sayhi():
	print("*" * 30)
	print("Hi")
	print("*" * 30)

	
>>> sayhi()
******************************
Hi
******************************
>>> def sayhi():
	print("Hi")

	
>>> def deco(f):
	def wrapper():
		print("*" * 30)
		f()
		print("*" * 30)
	return wrapper

>>> f = deco(sayhi)
>>> f()
******************************
Hi
******************************
>>> deco(sayhi)()
******************************
Hi
******************************
>>> def greet():
	print("Hello")

	
>>> deco(greet)()
******************************
Hello
******************************
>>> @deco
def sayhi():
	print("Hi")

	
>>> sayhi()
******************************
Hi
******************************
>>> @deco
def greet():
	print("Hello")

	
>>> greet()
******************************
Hello
******************************
>>> def deco2(f):
	def wrapper():
		print("-" * 30)
		f()
		print("-" * 30)
	return wrapper

>>> 
>>> @deco2
@deco
def sayhi():
	print("Hi")

	
>>> sayhi()
------------------------------
******************************
Hi
******************************
------------------------------
>>> 
