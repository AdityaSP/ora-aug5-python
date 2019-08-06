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
