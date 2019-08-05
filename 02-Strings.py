Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Strings
>>> s = "Hello World"
>>> type(s)
<class 'str'>
>>> s + " Again"
'Hello World Again'
>>> s1 = s + " Again"
>>> s1
'Hello World Again'
>>> s
'Hello World'
>>> #s = s + " Again"
>>> s += " Again"
>>> s
'Hello World Again'
>>> s
'Hello World Again'
>>> s + 3
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s + 3
TypeError: can only concatenate str (not "int") to str
>>> a = "5"
>>> b = 3
>>> a + b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a + b
TypeError: can only concatenate str (not "int") to str
>>> int(a) + b
8
>>> a + str(b)
'53'
>>> s = "Hello"
>>> s * 3
'HelloHelloHello'
>>> print("-" * 50)
--------------------------------------------------
>>> ############## String as sequence #############
>>> 
>>> 
>>> s = "Hello World"
>>> len(s)
11
>>> s[0]
'H'
>>> s[10]
'd'
>>> s[11]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s[11]
IndexError: string index out of range
>>> s[-1]
'd'
>>> s[-11]
'H'
>>> s[-12]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[-12]
IndexError: string index out of range
>>> 
>>> ### Slicing ###
>>> s
'Hello World'
>>> len(s)
11
>>> s[0:5]
'Hello'
>>> s[6:10]
'Worl'
>>> s[6:11]
'World'
>>> s[6:100]
'World'
>>> s[-1:-5]
''
>>> s[-5:-1]
'Worl'
>>> s[0:100:1]
'Hello World'
>>> s[0:100:2]
'HloWrd'
>>> s[-5:-1:1]
'Worl'
>>> s[-1:-5:1]
''
>>> s[-1:-5:-1]
'dlro'
>>> s
'Hello World'
>>> s[1:-1]
'ello Worl'
>>> s[6:-9]
''
>>> s[-1:0]
''
>>> s[0:-1]
'Hello Worl'
>>> s[-1:0:-1]
'dlroW olle'
>>> a = '0123456789'
>>> a[-1:0:-1]
'987654321'
>>> a[0:10:-1]
''
>>> a[-1:-10:-1]
'987654321'
>>> a[-1:-11:-1]
'9876543210'
>>> a[-1:-len(a)-1:-1]
'9876543210'
>>> a = "Hope lives on to let you hope"
>>> a[-1:-len(a)-1:-1]
'epoh uoy tel ot no sevil epoH'
>>> s
'Hello World'
>>> s[6:100]
'World'
>>> s[6:]
'World'
>>> s[6::2]
'Wrd'
>>> s[0:5]]
SyntaxError: invalid syntax
>>> s[0:5]
'Hello'
>>> s[:5]
'Hello'
>>> s[:]
'Hello World'
>>> s[::]
'Hello World'
>>> s[::-1]
'dlroW olleH'
>>> a = "Hope lives on to let you hope"
>>> a[-1:-len(a)-1:-1]
'epoh uoy tel ot no sevil epoH'
>>> a[::-1]
'epoh uoy tel ot no sevil epoH'
>>> # syntactic shorthand is also called as syntactic sugars
>>> 
