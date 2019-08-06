Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayhi():
	print("Hi")

	
>>> sayhi()
Hi
>>> x = sayhi()
Hi
>>> print(x, type(x))
None <class 'NoneType'>
>>> x = None
>>> id(x)
140717281983712
>>> def sayhi():
	print("Hi")
	return "Hi"

>>> x = sayhi()
Hi
>>> type(x)
<class 'str'>
>>> x
'Hi'
>>> s = '   hello  '
>>> s.strip()
'hello'
>>> s
'   hello  '
>>> def sayhi():
	return "Hi"

>>> def add(x,y):
	return x + y

>>> add(3,4)
7
>>> add(3,4) + 20 + add(5,6)
38
>>> 
>>> def full_name(fn, ln):
	return fn.capitalize() + " " + ln.capitalize()

>>> full_name('john','doe')
'John Doe'
>>> def full_name(fn, ln, title):
	return title.upper()+ "." + fn.capitalize() + " " + ln.capitalize()

>>> full_name('john','doe')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    full_name('john','doe')
TypeError: full_name() missing 1 required positional argument: 'title'
>>> full_name('john','doe', 'mr')
'MR.John Doe'
>>> def full_name(fn, ln, title='mr'):
	return title.upper()+ "." + fn.capitalize() + " " + ln.capitalize()

>>> full_name('john','doe')
'MR.John Doe'
>>> full_name('Aditya','Prabhakara','dr')
'DR.Aditya Prabhakara'
>>> full_name(fn='Aditya', ln='Prabhakara', title='dr')
'DR.Aditya Prabhakara'
>>> full_name(ln='Prabhakara', fn='Aditya', title='dr')
'DR.Aditya Prabhakara'
>>> full_name('Aditya', ln='Prabhakara')
'MR.Aditya Prabhakara'
>>> full_name(ln='Prabhakara', 'Aditya')
SyntaxError: positional argument follows keyword argument
>>> len.__doc__
'Return the number of items in a container.'
>>> sayhi.__doc__
>>> full_name.__doc__
>>> def sayhi():
	"this returns a cheerful Hi"
	return "Hi"

>>> sayhi.__doc__
'this returns a cheerful Hi'
>>> def full_name(fn, ln, title='mr'):
	"""*********
Takes in fn, ln title,
title is optional
returns back a formateed full name"""
	return title.upper()+ "." + fn.capitalize() + " " + ln.capitalize()

>>> full_name.__doc__
'*********\nTakes in fn, ln title,\ntitle is optional\nreturns back a formateed full name'
>>> help(full_name)
Help on function full_name in module __main__:

full_name(fn, ln, title='mr')
    *********
    Takes in fn, ln title,
    title is optional
    returns back a formateed full name

>>> l = [34,2,78,23,0]
>>> sorted(l)
[0, 2, 23, 34, 78]
>>> l
[34, 2, 78, 23, 0]
>>> sorted(l, reverse=True)
[78, 34, 23, 2, 0]
>>> l.sort(reverse=True)
>>> l
[78, 34, 23, 2, 0]
>>> sorted(iterable=l)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    sorted(iterable=l)
TypeError: sorted expected 1 arguments, got 0
>>> l.sort()
>>> l
[0, 2, 23, 34, 78]
>>> 
