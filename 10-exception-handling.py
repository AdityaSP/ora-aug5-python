Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> "hello"[7]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    "hello"[7]
IndexError: string index out of range
>>> def f(n):
	li = [1,2,3]
	1/n
	li[n]

	
>>> f(0)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    f(0)
  File "<pyshell#7>", line 3, in f
    1/n
ZeroDivisionError: division by zero
>>> f(1)
>>> f(4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    f(4)
  File "<pyshell#7>", line 4, in f
    li[n]
IndexError: list index out of range
>>> try:
	f(0)
except ZeroDivisionError as err:
	print("Not allowed", err)

	
Not allowed division by zero
>>> try:
	f(4)
except ZeroDivisionError as err:
	print("Not allowed", err)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    f(4)
  File "<pyshell#7>", line 4, in f
    li[n]
IndexError: list index out of range
>>> try:
	f(4)
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)

	
Wrong index list index out of range
>>> try:
	f(0)
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)

	
Not allowed division by zero
>>> try:
	f(6)
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)

	
Wrong index list index out of range
>>> try:
	f(f)
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    f(f)
  File "<pyshell#7>", line 3, in f
    1/n
TypeError: unsupported operand type(s) for /: 'int' and 'function'
>>> issubclass(ZeroDivisionError, Exception)
True
>>> try:
	f(f)
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)
except Exception as err:
	print("Was not expecting this", err)

	
Was not expecting this unsupported operand type(s) for /: 'int' and 'function'
>>> try:
	f(f)
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)
except Exception as err:
	print("Was not expecting this", err)
finally:
	print("Always executes")

	
Was not expecting this unsupported operand type(s) for /: 'int' and 'function'
Always executes
>>> try:
	f(2)
	
except ZeroDivisionError as err:
	print("Not allowed", err)
except IndexError as err:
	print("Wrong index", err)
except Exception as err:
	print("Was not expecting this", err)
finally:
	print("Always executes")

	
Always executes
>>> err = TypeError()
>>> raise err
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    raise err
TypeError
>>> err = TypeError("My own error")
>>> raise err
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    raise err
TypeError: My own error
>>> 
>>> 
>>> class MyOwnError(Exception):
	pass

>>> err = MyOwnError("New error type")
>>> raise err
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    raise err
MyOwnError: New error type
>>> raise MyOwnError("Newljjl;asf as")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    raise MyOwnError("Newljjl;asf as")
MyOwnError: Newljjl;asf as
>>> 
